import arcade
import random

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
BACKGROUND_COLOR = arcade.color.BLACK
GAME_TITLE = "Ada or Potato"
GAME_SPEED = 1 / 60

MAX_TIMER = 1 / GAME_SPEED

class AoPImage(arcade.Sprite):
    timer: int

    def __init__(self, image_name: str):
        super().__init__("images/" + image_name)
        self.timer = 0
        self.center_x = WINDOW_WIDTH / 2
        self.center_y = WINDOW_HEIGHT / 2
        if("potato" in image_name):
            self._set_scale(0.13)
        else:
            self._set_scale(0.6)

    def hide(self):
        self.kill()

class AdaOrPotatoGame(arcade.Window):
    timer: int
    score: int
    ada_image: arcade.Sprite
    potato_image: arcade.Sprite

    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, GAME_TITLE)
        self.sprite_list = None
        self.ada_image = AoPImage("ada.png")
        self.potato_image = AoPImage("potato.png")

    def setup(self):
        arcade.set_background_color(BACKGROUND_COLOR)
        self.sprite_list = arcade.SpriteList()

        self.timer = 0
        self.score = 0

    def set_random_image(self):
        self.ada_image.hide()
        self.potato_image.hide()
        if(random.random()>0.5):
            self.sprite_list.append(self.ada_image)
        else:
            self.sprite_list.append(self.potato_image)

    def on_draw(self):
        arcade.start_render()
        self.sprite_list.draw()
        self.update_text()

    def on_update(self, delta_time: float):
        if(self.timer < MAX_TIMER):
            self.timer += 1
        else:
            self.set_random_image()
            self.timer = 0

    def update_text(self):
        arcade.draw_text(f"Score: {self.score}", 5, 5, arcade.color.WHITE, 14)

    def on_mouse_press(self, x, y, button, modifiers):
        if(self.ada_image in self.sprite_list):
            self.score += 1
            self.timer = 0
            self.set_random_image()
        else:
            if(self.score>0):
                self.score -= 1
            self.timer = 0
            self.set_random_image()

def main():
    window = AdaOrPotatoGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()
