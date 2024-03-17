package routes

import (
	"github.com/gofiber/fiber/v2"
	"posts/controllers"
)

func Setup(app *fiber.App) {
	app.Get("/", controllers.GetPosts)
	app.Post("/", controllers.CreatePost)
	app.Get("/:uuid", controllers.GetPost)
	app.Put("/:uuid", controllers.UpdatePost)
	app.Delete("/:uuid", controllers.DeletePost)
}
