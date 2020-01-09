import random



class Snake:

    def __init__(self):
        self.segments = [(10,10)]
        self.speed = (-1, 0)
        self.desired_length = 5

    def update(self):
        """Moves the snake at the current speed, calculates positions of all segments"""
        ...

    def eat(self):
        """Start making the snake longer"""
        self.desired_length += 4

    def collission(self):
        """Returns True if the snake collided with itself"""






alien = Actor('alien')
alien2= Actor('alien')


alien2.pos = 650,650
alien.pos = 100, 56
use_small_alien_for_ammunition = Actor('rocket')
use_small_alien_for_ammunition.pos = -100, -300
# TOP SECRET CODENAME
usafa = use_small_alien_for_ammunition
usafa.inflate_ip(1, 1)
usafa.angle = 7

WIDTH = 740
HEIGHT = 740


def draw():
    screen.clear()
    alien.draw()
    use_small_alien_for_ammunition.draw()
    alien2.draw()



def on_mouse_down(pos):
    use_small_alien_for_ammunition.pos = pos
    use_small_alien_for_ammunition.angle = 45

    if alien.collidepoint(pos):
        print("I should say eek but this doesn't really hurt me. However, going beyond eighty characters will hurt some people who read this.")
    else:
        print("You missed me!")

ROCKET_SPEED = 4

def update():
    rocket_x, rocket_y = usafa.pos
    usafa.pos = (rocket_x+ROCKET_SPEED, rocket_y+ROCKET_SPEED)
    usafa.angle += 10

    if usafa.colliderect(alien2):
        alien2.pos = 900, 900
        print("Whoops, that hurt. But I'll be back (randomly, maybe).")

    alien2_x, alien2_y = alien2.pos
    alien2.pos = random.choice ([-5,0,5] ) + alien2_x, random.choice ([-5,0,5] ) + alien2_y

 
