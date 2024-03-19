package main

import (
	"github.com/gofiber/fiber/v2"
	"github.com/joho/godotenv"
	db "posts/config"
	"posts/middlewares"
	"posts/routes"
)

func main() {
	println("Loading Environment Variables...")
	err := godotenv.Load()

	if err != nil {
		panic("Could not load the environment variables...")
	}

	db.ConnectPostgres()
	db.ConnectRedis()

	app := fiber.New()
	app.Use(middlewares.AuthMiddleware)
	routes.Setup(app)

	err = app.Listen(":3000")
	if err != nil {
		panic("Could not start the server...")
	}
}
