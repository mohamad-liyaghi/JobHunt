package controllers

import (
	"github.com/gofiber/fiber/v2"
	db "posts/config"
	"posts/models"
	"strconv"
	"time"
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
	// get userId from context
	userId := c.Locals("userId").(int)
	var data map[string]string
	if err := c.BodyParser(&data); err != nil {
		return c.Status(fiber.StatusBadRequest).JSON(fiber.Map{
			"message": "Invalid JSON",
		})
	}

	if data["title"] == "" || data["description"] == "" {
		return c.Status(fiber.StatusBadRequest).JSON(fiber.Map{
			"message": "Title and Description are required",
		})
	}

	post := models.Post{
		UserId:      userId,
		Title:       data["title"],
		Description: data["description"],
		CreatedAt:   time.Now(),
	}

	db.DB.Create(&post)

	return c.Status(fiber.StatusCreated).JSON(fiber.Map{
		"message": "Post created successfully",
		"post":    post,
	})
}

func GetPost(c *fiber.Ctx) error {
	var post models.Post
	id, _ := strconv.Atoi(c.Params("id"))
	db.DB.First(&post, id)
	if post == (models.Post{}) {
		return c.Status(fiber.StatusNotFound).JSON(fiber.Map{
			"message": "Post not found",
		})
	}
	return c.Status(fiber.StatusOK).JSON(post)

}

func UpdatePost(c *fiber.Ctx) error {
	userId := c.Locals("userId").(int)
	id, _ := strconv.Atoi(c.Params("id"))
	var post models.Post
	db.DB.First(&post, id)
	if post == (models.Post{}) {
		return c.Status(fiber.StatusNotFound).JSON(fiber.Map{
			"message": "Post not found",
		})
	}
	if post.UserId != userId {
		return c.Status(fiber.StatusUnauthorized).JSON(fiber.Map{
			"message": "You are not authorized to update this post",
		})
	}

	var data map[string]string
	if err := c.BodyParser(&data); err != nil {
		return c.Status(fiber.StatusBadRequest).JSON(fiber.Map{
			"message": "Invalid JSON",
		})
	}

	if data["title"] == "" || data["description"] == "" {
		return c.Status(fiber.StatusBadRequest).JSON(fiber.Map{
			"message": "Title and Description are required",
		})
	}

	db.DB.Model(&post).Updates(models.Post{
		Title:       data["title"],
		Description: data["description"],
	})

	return c.Status(fiber.StatusOK).JSON(fiber.Map{
		"message": "Post updated successfully",
		"post":    post,
	})
}

func DeletePost(c *fiber.Ctx) error {
	userId := c.Locals("userId").(int)
	id, _ := strconv.Atoi(c.Params("id"))
	var post models.Post
	db.DB.First(&post, id)
	if post == (models.Post{}) {
		return c.Status(fiber.StatusNotFound).JSON(fiber.Map{
			"message": "Post not found",
		})
	}
	if post.UserId != userId {
		return c.Status(fiber.StatusUnauthorized).JSON(fiber.Map{
			"message": "You are not authorized to delete this post",
		})
	}

	db.DB.Delete(&post)
	return c.Status(fiber.StatusNoContent).JSON(fiber.Map{
		"message": "Post deleted successfully",
	})
}
