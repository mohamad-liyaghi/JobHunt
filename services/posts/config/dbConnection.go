package db

import (
	"github.com/joho/godotenv"
	"gorm.io/driver/postgres"
	"gorm.io/gorm"
	"os"
	"posts/models"
)

var DB *gorm.DB

func ConnectPostgres() *gorm.DB {
	err := godotenv.Load()
	if err != nil {
		return nil
	}
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
		DB = db
		AutoMigration(DB)
		return DB
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
