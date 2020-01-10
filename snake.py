import random
import sys

WIDTH = 600
HEIGHT = 600

food = Actor('food_tiny', center=(random.randrange(WIDTH), random.randrange(HEIGHT)))
snake = [Actor('snake_head_tiny')]

snake_speed = (-1, 0)

def grow_snake(amount=3):
    last_position = snake[-1].center
    for i in range(amount):
        snake.append(Actor('snake_body_tiny', center=last_position))

grow_snake(3)

def draw():
    screen.clear()
    food.draw()
    for snake_part in snake:
        snake_part.draw()

def snake_is_colliding():
    """Returns True if the snake collided with itself"""
    if snake[0].collidelist(snake[1:]) > 0:
        return True

def snake_is_eating():
    """Returns True if the snake is eating food"""
    if snake[0].colliderect(food):
        return True

def move_snake():
    old_head_x, old_head_y = snake[0].center
    new_head_position = ((old_head_x + snake_speed[0] * snake[0].width) % WIDTH,
        (old_head_y + snake_speed[1] * snake[0].height) % HEIGHT)
    
    for i in range(len(snake) - 1, 0, -1):
        snake[i].center = snake[i-1].center
    snake[0].center = new_head_position

    if snake_is_colliding():
        print("YOU LOSE!")
        sys.exit(1)

    if snake_is_eating():
        grow_snake(3)
        animate(food, pos=(random.randrange(20, WIDTH-20), random.randrange(20,HEIGHT-20)))

clock.schedule_interval(move_snake, 0.4)

def on_key_down(key, *args):
    global snake_speed
    if key == keys.DOWN:
        snake_speed = (0, 1)
    elif key == keys.UP:
        snake_speed = (0, -1)
    elif key == keys.LEFT:
        snake_speed = (-1, 0)
    elif key == keys.RIGHT:
        snake_speed = (1, 0)
