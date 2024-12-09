import pygame
from sys import exit

# Initialize Pygame (always needed before any other Pygame code)
pygame.init()

# Create the game window with dimensions 800x400 pixels
screen = pygame.display.set_mode((1600,800))

## game window icon setup
icon = pygame.image.load('game_icon.jpg') #sets the location of icon
pygame.display.set_icon(icon) #set the game window icon
pygame.display.set_caption('Wealth of The Fields') # Set the title of the game window

# Main game loop
while True:
    # Event handling loop
    for event in pygame.event.get():
        # Check if the user closes the window
        if event.type == pygame.QUIT:
            pygame.quit()  # Uninitialize all Pygame modules
            exit()  # Exit the program entirely (more reliable than break)

    
    pygame.display.update() # Update the display