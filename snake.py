import random

WORLD_WIDTH = 60
WORLD_HEIGHT = 40


class Snake:

    def __init__(self):
        self.segments = [(10,10)]
        self.speed = (-1, 0)
        self.desired_length = 5

    def update(self):
        """Moves the snake at the current speed, calculates positions of all segments"""
        old_head_x, old_head_y = self.segments[0]
        head = ((old_head_x + self.speed[0]) % WORLD_WIDTH,
                (old_head_y + self.speed[1]) % WORLD_HEIGHT)
        self.segments.insert(0, head)
        self.segments = self.segments[:self.desired_length]

    def eat(self):
        """Start making the snake longer"""
        self.desired_length += 4

    def collission(self):
        """Returns True if the snake collided with itself"""
        return self.segments[0] in self.segments[1:]


WIDTH = 740
HEIGHT = 740
grid_width = 37
grid_height = 37
section_size = WIDTH / grid_width

grid = Snake()

def draw():
    screen.clear()
    snake_segments = [Actor('alien') for segment in grid.segments]
    for num, segment in enumerate(grid.segments):
        seg = snake_segments[num]
        seg.pos = segment[0] * section_size, segment[1] * section_size
        seg.draw()
    grid.update()
