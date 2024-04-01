package routes

import (
	"github.com/gofiber/fiber/v2"
	"posts/controllers"
)

func Setup(app *fiber.App) {
	app.Get("/", controllers.GetPosts)
	app.Post("/", controllers.CreatePost)
	app.Get("/:id", controllers.GetPost)
	app.Put("/:id", controllers.UpdatePost)
	app.Delete("/:id", controllers.DeletePost)
}
