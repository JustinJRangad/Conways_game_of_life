import pygame
import numpy as np

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

# Dimensions
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 80, 80
CELL_SIZE = WIDTH // COLS

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Create the grid
grid = np.zeros((ROWS, COLS), dtype=int)

# Flag variable to control game running state
game_running = False

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the cell position based on the mouse click
            x, y = pygame.mouse.get_pos()
            col = x // CELL_SIZE
            row = y // CELL_SIZE

            # Toggle the state of the clicked cell
            grid[row, col] = 1 - grid[row, col]
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
            elif event.key == pygame.K_SPACE:
                game_running = not game_running

    if game_running:
        # Update the grid
        new_grid = np.copy(grid)
        for i in range(ROWS):
            for j in range(COLS):
                neighbors = np.sum(grid[i - 1:i + 2, j - 1:j + 2]) - grid[i, j]

                # Apply the rules of Conway's Game of Life
                if grid[i, j] == 1 and (neighbors < 2 or neighbors > 3):
                    new_grid[i, j] = 0
                elif grid[i, j] == 0 and neighbors == 3:
                    new_grid[i, j] = 1

        grid = new_grid

    # Draw the grid
    screen.fill(BLACK)
    for i in range(ROWS):
        for j in range(COLS):
            if grid[i, j] == 1:
                pygame.draw.rect(screen, WHITE, (j * CELL_SIZE,
                                 i * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            else:
                pygame.draw.rect(screen, GRAY, (j * CELL_SIZE,
                                 i * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

    # Draw the quit button
    pygame.draw.rect(screen, GRAY, (WIDTH - 100, HEIGHT - 50, 80, 30))
    quit_text = pygame.font.SysFont(None, 24).render("Quit", True, WHITE)
    screen.blit(quit_text, (WIDTH - 90, HEIGHT - 45))

    # Update the display
    pygame.display.flip()
    clock.tick(10)  # Set the desired FPS

# Quit the game
pygame.quit()
