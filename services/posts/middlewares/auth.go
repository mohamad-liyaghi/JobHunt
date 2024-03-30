package middlewares

import (
	"encoding/json"
	"github.com/gofiber/fiber/v2"
	"io/ioutil"
	"net/http"
	jwt "posts/handlers"
)

func AuthMiddleware(c *fiber.Ctx) error {
	authHeader := c.Get("Authorization")

	// Check for Authorization header
	if authHeader == "" {
		return c.Status(fiber.StatusUnauthorized).SendString("Unauthorized")
	}

	validationURL := "http://user-backend:8000/v1/profiles/me/"
	validationRequest, err := http.NewRequest("GET", validationURL, nil)
	validationRequest.Header.Set("Authorization", authHeader)
	validationResponse, err := http.DefaultClient.Do(validationRequest)

	defer validationResponse.Body.Close()
	body, err := ioutil.ReadAll(validationResponse.Body)

	var user jwt.User
	err = json.Unmarshal(body, &user)

	// Store user_id in Locals
	c.Locals("user_id", user.ID)

	if err != nil {
		return c.Status(fiber.StatusInternalServerError).SendString("Internal server error")
	}

	if validationResponse.StatusCode != http.StatusOK {
		return c.Status(fiber.StatusForbidden).SendString("Forbidden")
	}

	return c.Next()
}
