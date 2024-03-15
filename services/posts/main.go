package main

import (
	"github.com/gofiber/fiber/v2"
	"github.com/joho/godotenv"
	"gorm.io/driver/postgres"
	"gorm.io/gorm"
	"os"
)

var DB *gorm.DB

func main() {
	godotenv.Load()
	postgresDB := os.Getenv("POSTGRES_DB")
	postgresUser := os.Getenv("POSTGRES_USER")
	postgresPassword := os.Getenv("POSTGRES_PASSWORD")
	postgresHost := os.Getenv("POSTGRES_HOST")
	postgresPort := os.Getenv("POSTGRES_PORT")
	connection := "host=" + postgresHost + " port=" + postgresPort + " user=" + postgresUser + " dbname=" + postgresDB + " password=" + postgresPassword + " sslmode=disable"
	db, err := gorm.Open(postgres.Open(connection), &gorm.Config{})

	if err != nil {
		panic("Could not connect to the database...")
	} else {
		DB = db
	}

	app := fiber.New()

	app.Listen(":3000")
}
