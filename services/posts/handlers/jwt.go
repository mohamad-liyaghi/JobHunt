package jwt

import (
	"fmt"
	"github.com/dgrijalva/jwt-go"
	"github.com/joho/godotenv"
	"os"
	"strings"
	"time"
)

type User struct {
	ID   int
	UUID string
}

func DecodeToken(tokenString string) (User, error) {
	godotenv.Load()
	secretKey := os.Getenv("SECRET_KEY")

	tokenString = strings.Replace(tokenString, "Bearer ", "", 1)

	token, err := jwt.Parse(tokenString, func(token *jwt.Token) (interface{}, error) {
		if _, ok := token.Method.(*jwt.SigningMethodHMAC); !ok {
			return nil, fmt.Errorf("Unexpected signing method: %v", token.Header["alg"])
		}
		return []byte(secretKey), nil
	})

	// Check for errors
	if err != nil {
		return User{}, err
	}

	// Validate the token
	if !token.Valid {
		return User{}, fmt.Errorf("Invalid token")
	}

	// Extract claims
	claims, ok := token.Claims.(jwt.MapClaims)
	if !ok {
		return User{}, fmt.Errorf("Failed to parse claims")
	}

	// Extract user_id and valid_until from claims
	userID, ok := claims["user_id"]
	if !ok {
		return User{}, fmt.Errorf("Missing or invalid user_id claim")
	}

	userUUID, ok := claims["user_uuid"].(string)
	if !ok {
		return User{}, fmt.Errorf("Missing or invalid user_uuid claim")
	}

	validUntilFloat64, ok := claims["exp"].(float64)
	if !ok {
		return User{}, fmt.Errorf("Missing or invalid valid_until claim")
	}

	validUntil := time.Unix(int64(validUntilFloat64), 0)

	// Check validity by time
	if time.Now().After(validUntil) {
		return User{}, fmt.Errorf("Token has expired")
	}

	// make user id int from interface
	userIDInt, ok := userID.(float64)

	return User{ID: int(userIDInt), UUID: userUUID}, nil
}
