package main

import (
	"github.com/gofiber/fiber/v2"
	"github.com/joho/godotenv"
	"github.com/redis/go-redis/v9"
	"gorm.io/driver/postgres"
	"gorm.io/gorm"
	"os"
	"posts/middlewares"
	"posts/models"
	"posts/routes"
)

var DB *gorm.DB
var Redis *redis.Client

func main() {
	println("Loading Environment Variables...")
	err := godotenv.Load()

	if err != nil {
		panic("Could not load the environment variables...")
	}

	DB = ConnectPostgres()
	AutoMigration(DB)
	Redis = ConnectRedis()

	app := fiber.New()
	app.Use(middlewares.AuthMiddleware)
	routes.Setup(app)

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

func ConnectPostgres() *gorm.DB {
	println("Connecting to the database...")
	postgresDB := os.Getenv("POSTGRES_DB")
	postgresUser := os.Getenv("POSTGRES_USER")
	postgresPassword := os.Getenv("POSTGRES_PASSWORD")
	postgresHost := os.Getenv("POSTGRES_HOST")
	postgresPort := os.Getenv("POSTGRES_PORT")
	connection := "host=" + postgresHost + " user=" + postgresUser + " password=" + postgresPassword + " dbname=" + postgresDB + " port=" + postgresPort
	db, err := gorm.Open(postgres.Open(connection), &gorm.Config{})

	if err != nil {
		panic("Could not connect to the database...")
	} else {
		return db
	}
}

func ConnectRedis() *redis.Client {
	println("Connecting to Redis...")
	redisHost := os.Getenv("REDIS_HOST")
	redisPort := os.Getenv("REDIS_PORT")
	redisPassword := os.Getenv("REDIS_PASSWORD")

	redisClient := redis.NewClient(&redis.Options{
		Addr:     redisHost + ":" + redisPort,
		Password: redisPassword,
		DB:       0,
	})
	return redisClient
}
