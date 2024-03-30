package jwt

import (
	"github.com/joho/godotenv"
	"os"
)

func DecodeToken(token string) (*jwt.Token, error) {
	godotenv.Load()
	secret_key := os.Getenv("SECRET_KEY")
	json, err :=
}
