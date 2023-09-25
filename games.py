import pygame

# Initialize Pygame
pygame.init()

# Set the screen size
screen = pygame.display.set_mode((400, 300))

# Set the title of the window
pygame.display.set_caption("My Game")

# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color
    screen.fill((0, 0, 0))

    # Draw a circle on the screen
    pygame.draw.circle(screen, (255, 255, 255), (200, 150), 50)

    # Update the screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()