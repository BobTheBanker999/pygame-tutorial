# Import needed modules
import pygame
import random # We will need this for later
from pygame.locals import *

# Create constants for screen width and height
SCREEN_W = 800
SCREEN_H = 600

# Initialize pygame
pygame.init()

# Set up the clock
clock = pygame.time.Clock()

# Create screen
screen = pygame.display.set_mode([SCREEN_W, SCREEN_H])
# Set Screen title
pygame.display.set_caption("CAPTION HERE") # Put your caption here

# Boolean to keep Main loop running
running = True

# Main loop
while running:

    # Scan all game events
    for event in pygame.event.get():

        # Quit if user closes the window or presses ESC.
        if event.type == QUIT:
            print("Why did you leave me, buddy? :(")
            pygame.quit()
        
        # Look for keypresses
        key = pygame.key.get_pressed()
        
        if key[K_ESCAPE]:
            print("Why did you leave me, buddy? :(")
            pygame.quit()
