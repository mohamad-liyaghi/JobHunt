package db

import (
	"context"
	"github.com/joho/godotenv"
	"github.com/redis/go-redis/v9"
	"os"
)

var Redis *redis.Client
var RedisCtx = context.Background()

func ConnectRedis() *redis.Client {
	err := godotenv.Load()
	if err != nil {
		return nil
	}
	println("Connecting to Redis...")
	redisHost := os.Getenv("REDIS_HOST")
	redisPort := os.Getenv("REDIS_PORT")
	redisPassword := os.Getenv("REDIS_PASSWORD")

	redisClient := redis.NewClient(&redis.Options{
		Addr:     redisHost + ":" + redisPort,
		Password: redisPassword,
		DB:       0,
	})
	Redis = redisClient
	return Redis
}
