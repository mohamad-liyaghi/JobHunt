package controllers

import "github.com/gofiber/fiber/v2"

func GetPosts(c *fiber.Ctx) error {
	return c.SendString("Get Post Route!")
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
