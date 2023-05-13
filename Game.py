# Install Pygame: Pygame is a popular Python library for creating games.
# You can install it using pip with the command pip install pygame.
# Set up the game window: Create a Pygame window with the desired size and caption.

import pygame
import random
pygame.init()

# Set up the window
width = 500
height = 500
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Set up the game loop:
# Create a game loop that updates the game state and renders the game on the screen.

# Set up the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update game state

    # Render game
    pygame.display.update()

# Create the snake: Create a list of rectangles that represent the snake's body.

# Create the snake
snake_size = 10
snake = [pygame.Rect(width/2, height/2, snake_size, snake_size)]

# Move the snake: Move the snake in response to user input or a timer.

# Move the snake
keys = pygame.key.get_pressed()
if keys[pygame.K_LEFT]:
    snake[0].x -= snake_size
if keys[pygame.K_RIGHT]:
    snake[0].x += snake_size
if keys[pygame.K_UP]:
    snake[0].y -= snake_size
if keys[pygame.K_DOWN]:
    snake[0].y += snake_size

# Draw the snake: Draw the snake on the screen.

# Draw the snake
for rect in snake:
    pygame.draw.rect(window, (255, 255, 255), rect)

# Add food: Add food to the game that the snake can eat.

# Add food
food_size = 10
food = pygame.Rect(0, 0, food_size, food_size)
food.x = random.randint(0, width - food_size)
food.y = random.randint(0, height - food_size)

# Draw food
pygame.draw.rect(window, (255, 0, 0), food)
