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
	println("Loading Environment Variables...")
	postgresDB := os.Getenv("POSTGRES_DB")
	postgresUser := os.Getenv("POSTGRES_USER")
	postgresPassword := os.Getenv("POSTGRES_PASSWORD")
	postgresHost := os.Getenv("POSTGRES_HOST")
	postgresPort := os.Getenv("POSTGRES_PORT")

	println("Connecting to the database...")
	connection := "host=" + postgresHost + " user=" + postgresUser + " password=" + postgresPassword + " dbname=" + postgresDB + " port=" + postgresPort
	db, err := gorm.Open(postgres.Open(connection), &gorm.Config{})

	if err != nil {
		panic("Could not connect to the database...")
	} else {
		DB = db
		println("Connected to the database...")
	}

	app := fiber.New()

	app.Listen(":3000")
}
