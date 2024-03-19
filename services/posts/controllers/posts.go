package controllers

import (
	"github.com/gofiber/fiber/v2"
	db "posts/config"
	"posts/models"
	"strconv"
)

func GetPosts(c *fiber.Ctx) error {
	var posts []models.Post
	limit, _ := strconv.Atoi(c.Query("limit", "10"))
	offset, _ := strconv.Atoi(c.Query("offset", "0"))
	var count int64

	db.DB.Select("title", "created_at").Limit(limit).Offset(offset).Find(&posts).Count(&count).Order("created_at desc")
	return c.Status(fiber.StatusOK).JSON(fiber.Map{
		"posts": posts,
		"total": count,
	})
}

func CreatePost(c *fiber.Ctx) error {
	return c.SendString("Create Post Route!")
}

func GetPost(c *fiber.Ctx) error {
	return c.SendString("Get Post Route!")
}

func UpdatePost(c *fiber.Ctx) error {
	return c.SendString("Update Post Route!")
}

func DeletePost(c *fiber.Ctx) error {
	return c.SendString("Delete Post Route!")
}
