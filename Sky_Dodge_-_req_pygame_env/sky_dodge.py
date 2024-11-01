# Import the pygame module
import pygame

# Import the random module
import random

# Import timer
from time import time

# Import OS
import os

# Import pygame.locals for easier access to key coordinates
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Define constants for the screen width and height
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

# Define a Player class by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("images/jet.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()

    # Move the sprite based on user key presses
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
            move_up_sound.play()
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
            move_down_sound.play()
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
        
        # Keep player on screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

# Define the enemy class by extending pygame.sprite.Sprite
# The surface you draw on screen is now an attribute of 'enemy'
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load("images/missile.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT)
            )
        )
        self.speed = random.randint(5, 20)

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

# Define the Cloud class by extending pygame.sprite.Sprite
class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        self.surf = pygame.image.load("images/cloud.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        # The starting position is randomly generated
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT)
            )
        )
    
    # Move the cloud based on constant speed
    # Remove cloud when it passes left edge of screen
    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()


# Initialize music and sounds mixer
pygame.mixer.init()

# Initialize pygame
pygame.init()

# Set up the clock for a playable frame rate
clock = pygame.time.Clock()


# Create the screen object
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Create a custom event for adding a new enemy and new cloud
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)
ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 1000)

# Instantiate player
player = Player()

# Create groups to hold enemy sprites and all sprites
# - enemies is used for collision detection and position updates
# - all_sprites is used for rendering
enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Load and play background music
# Sound source: Chris Bailey - artist Tripnet
# License: https://creativecommons.org/licenses/by/3.0/
pygame.mixer.music.load("sound/Sky_dodge_theme.ogg")
pygame.mixer.music.play(loops=-1)
pygame.mixer.music.set_volume(0.4)

# Load sound effects
# Sound source: Chris Bailey
move_up_sound = pygame.mixer.Sound("sound/Jet_up.ogg")
move_down_sound = pygame.mixer.Sound("sound/Jet_down.ogg")
collision_sound = pygame.mixer.Sound("sound/Boom.ogg")

# Adjust the volume of the sound effects
move_up_sound.set_volume(0.6)
move_down_sound.set_volume(0.6)
collision_sound.set_volume(1.0)

# Variable to keep the main loop running
running = True

# Start timer
start_time = time()

# Main loop
while running:
    # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the ESC key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False
        
        # Did the user click the window close button? If yes, stop.
        elif event.type == QUIT:
            running = False
        
        # Add a new enemy?
        elif event.type == ADDENEMY:
            # Create a new enemy and add it to the sprite groups
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

        # Add a new cloud?
        elif event.type == ADDCLOUD:
            # Create a new cloud and it to the sprite groups
            new_cloud = Cloud()
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)

    # Get the set of keys pressed and check user input and then update.
    # This is a set of all keyboard keys with Boolean status for each.
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)

    # Update enemy and cloud position
    enemies.update()
    clouds.update()

    # Fill in the screen with sky blue
    screen.fill((135, 206, 250))

    # Draw all sprites on screen
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    # Check if any enemies have collided with the player
    if pygame.sprite.spritecollideany(player, enemies):
        # If so, remove the player and stop the loop
        player.kill()

        # Stop any moving sounds, music and then play the collision sound
        move_up_sound.stop()
        move_down_sound.stop()
        pygame.mixer.music.stop()
        screen.fill((255, 0, 0))
        pygame.time.delay(50)
        collision_sound.play()
        pygame.time.delay(800)

        # Stop the loop
        running = False

    # Update the display
    pygame.display.flip()

    # Ensure the clock maintains max 30 fps
    clock.tick(30) 


# Done. Quit program.
pygame.mixer.quit()
pygame.quit()

# Calculate elapsed time
end_time = time()

# Load best time
with open("best_time.txt", "r") as f:
    best_time = float(f.readline())

# Print best time
os.system("cls" if os.name == "nt" else "clear")
print(f"Your best time is {best_time} seconds.")
elapsed_time = round(end_time - start_time, 3)
print(f"You lasted {elapsed_time} seconds.")

# Check if new best time?
if elapsed_time > best_time:
    print("\nNEW RECORD! WELL DONE!")
    with open("best_time.txt", "w") as f:
        f.write(str(elapsed_time))

print("\nGoodbye.")
