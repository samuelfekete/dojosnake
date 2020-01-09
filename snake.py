import random

WORLD_WIDTH = 60
WORLD_HEIGHT = 40


class SnakeGrid:

    def __init__(self):
        self.segments = [(10,10)]
        self.speed = (-1, 0)
        self.desired_length = 5
        self.grid_width = 37
        self.grid_height = 37
        self.clock = 0.0

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

grid = SnakeGrid()
section_size = WIDTH / grid.grid_width

def draw():
    screen.clear()
    snake_segments = []
    snake_segments.append(Actor('snake_head_tiny'))
    for i in range(len(grid.segments) - 1):
        snake_segments.append(Actor('snake_body_tiny'))
    for num, segment in enumerate(grid.segments):
        seg = snake_segments[num]
        seg.pos = segment[0] * section_size, segment[1] * section_size
        seg.draw()
    snake_segments[0].draw()

def update(dt):
    TICK_DURATION = 0.1
    grid.clock += dt
    if grid.clock > TICK_DURATION:
        grid.clock -= TICK_DURATION
        grid.update()

def on_key_down(key, *args):
    if key == keys.DOWN:
        grid.speed = (0, 1)
    elif key == keys.UP:
        grid.speed = (0, -1)
    elif key == keys.LEFT:
        grid.speed = (-1, 0)
    elif key == keys.RIGHT:
        grid.speed = (1, 0)
    elif key == keys.SPACE:
        grid.eat()
