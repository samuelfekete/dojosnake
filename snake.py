import random

WIDTH = 629
HEIGHT = 629

RIGHT = 90
UP = 180
LEFT = 270
DOWN = 360

food = Actor('food_tiny', center=(WIDTH/2, HEIGHT/2))
snake_head = Actor('snake_head_tiny', left=0, top=0)
snake = [snake_head]

snake_head.direction = RIGHT
snake_head.angle = RIGHT
snake_head.alive = True

def grow_snake():
    last_position = snake[-1].center
    snake.append(Actor('snake_body_tiny', center=last_position))

grow_snake()

def draw():
    screen.clear()
    if not snake_head.alive:
        screen.draw.text(
            "YOU LOSE!",
            center=(WIDTH/2, HEIGHT/2),
            fontsize=64
        )
    else:
        food.draw()
        for snake_part in snake:
            snake_part.draw()

def snake_is_colliding():
    """Returns True if the snake collided with itself or the edges"""
    
    if snake_head.collidelist(snake[1:]) > 0:
        return True
    
    if snake_over_edge():
        return True

def snake_is_eating():
    """Returns True if the snake is eating food"""
    
    if snake_head.colliderect(food):
        return True

def snake_over_edge():
    """Returns true if the snake is over the edge."""
    
    if snake_head.left < 0:
        return True
    
    if snake_head.top < 0:
        return True
    
    if snake_head.right > WIDTH:
        return True
    
    if snake_head.bottom > HEIGHT:
        return True

def move_snake():
    """Move the snake to the next position."""

    for i in range(len(snake) - 1, 0, -1):
        snake[i].center = snake[i-1].center

    if snake_head.direction == LEFT:
        snake_head.right = snake_head.left

    if snake_head.direction == RIGHT:
        snake_head.left = snake_head.right

    if snake_head.direction == UP:
        snake_head.bottom = snake_head.top

    if snake_head.direction == DOWN:
        snake_head.top = snake_head.bottom

    if snake_is_colliding():
        snake_head.alive = False

    if snake_is_eating():
        grow_snake()
        animate(
            food,
            pos=(
                random.randrange(food.width, WIDTH - food.width),
                random.randrange(food.width, HEIGHT - food.width)),
            tween="in_out_elastic",
            duration=0.5,
        )

def on_key_down(key, *args):
    """Handle a key being pressed."""
    
    if key == keys.DOWN:
        snake_head.direction = DOWN
        snake_head.angle = DOWN
    
    if key == keys.UP:
        snake_head.direction = UP
        snake_head.angle = UP
    
    if key == keys.LEFT:
        snake_head.direction = LEFT
        snake_head.angle = LEFT
    
    if key == keys.RIGHT:
        snake_head.direction = RIGHT
        snake_head.angle = RIGHT

clock.schedule_interval(move_snake, 0.3)
