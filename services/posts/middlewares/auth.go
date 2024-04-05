package middlewares

import (
	"encoding/json"
	"github.com/gofiber/fiber/v2"
	"io/ioutil"
	"net/http"
	db "posts/config"
	jwt "posts/handlers"
	"strconv"
	"time"
)

func AuthMiddleware(c *fiber.Ctx) error {
	authHeader := c.Get("Authorization")

	if authHeader == "" {
		return c.Status(fiber.StatusUnauthorized).SendString("Unauthorized")
	}
	jwtUser, _ := jwt.DecodeToken(authHeader)
	userId := jwtUser.ID

	// check if user is in redis
	_, err := db.Redis.Get(db.RedisCtx, strconv.Itoa(userId)).Result()

	if err != nil {
		validationURL := "http://user-backend:8000/v1/profiles/me/"
		validationRequest, err := http.NewRequest("GET", validationURL, nil)
		validationRequest.Header.Set("Authorization", authHeader)
		validationResponse, err := http.DefaultClient.Do(validationRequest)

		defer validationResponse.Body.Close()
		body, err := ioutil.ReadAll(validationResponse.Body)

		var user jwt.User
		err = json.Unmarshal(body, &user)
		if err != nil {
			return c.Status(fiber.StatusInternalServerError).SendString("Internal server error")
		}

		if validationResponse.StatusCode != http.StatusOK {
			return c.Status(fiber.StatusForbidden).SendString("Forbidden")
		}
		_, err = db.Redis.Set(db.RedisCtx, strconv.Itoa(userId), string(body), 15*time.Minute).Result()

	}

	// Store user_id in Locals
	c.Locals("userId", jwtUser.ID)

	return c.Next()
}
