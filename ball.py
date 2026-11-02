from pico2d import load_image, get_canvas_width
import game_world


class Ball:
    def __init__(self, x, y, direction):
        self.x, self.y = x, y
        self.direction = direction
        self.image = load_image('ball21x21.png')

    def update(self):
        self.x += self.direction * 10
        if self.x < 0 or self.x > get_canvas_width():
            game_world.remove_object(self)

    def draw(self):
        self.image.draw(self.x, self.y)
