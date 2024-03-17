package middlewares

import (
	"github.com/gofiber/fiber/v2"
	"net/http"
	"net/url"
)

func AuthMiddleware(c *fiber.Ctx) error {
	authHeader := c.Get("Authorization")

	// Check for Authorization header
	if authHeader == "" {
		return c.Status(fiber.StatusUnauthorized).SendString("Unauthorized")
	}

	validationURL := "http://users:8000/profiles/me/"
	formData := url.Values{"token": {authHeader}}
	validationResponse, err := http.PostForm(validationURL, formData)

	if err != nil {
		// Handle communication error gracefully
		return c.Status(fiber.StatusInternalServerError).SendString("Internal server error")
	}

	defer validationResponse.Body.Close()

	// Check validation response
	if validationResponse.StatusCode != http.StatusOK {
		return c.Status(fiber.StatusForbidden).SendString("Forbidden")
	}

	// Forward request if authentication is successful
	return c.Next()
}
