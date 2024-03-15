package main

import (
	"github.com/gofiber/fiber/v2"
	"github.com/joho/godotenv"
	"gorm.io/driver/postgres"
	"gorm.io/gorm"
	"os"
	"posts/models"
)

var DB *gorm.DB

func main() {
	err := godotenv.Load()

	if err != nil {
		panic("Could not load the environment variables...")
	}

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

	AutoMigration(DB)

	app := fiber.New()
	err = app.Listen(":3000")
	if err != nil {
		panic("Could not start the server...")
	}
}

func AutoMigration(connection *gorm.DB) {
	println("Applying Migrations...")
	err := connection.Debug().AutoMigrate(
		&models.Post{},
	)
	if err != nil {
		panic("Could not migrate the database...")
	} else {
		println("Database migrated...")
	}
}
