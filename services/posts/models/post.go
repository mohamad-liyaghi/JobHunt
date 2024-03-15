package models

import (
	"time"
)

type Post struct {
	ID          int       `json:"id"`
	UserId      int       `json:"user_id"`
	Title       string    `json:"title"`
	Description string    `json:"description"`
	CreatedAt   time.Time `json:"created_at"`
}
