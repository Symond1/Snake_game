import pygame
import time
import random

# Initialize pygame
pygame.init()

# Define colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Set screen dimensions
width = 600
height = 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Load background image and scale it to fill the screen
background_img = pygame.image.load('background.jpg')  
background_img = pygame.transform.scale(background_img, (width, height))

# Define clock and snake block size
snake_block = 15
snake_speed = 15  

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 20)  

def Your_score(score):
    value = score_font.render("Score: " + str(score), True, yellow)
    screen.blit(value, [10, 10])  

def our_snake(snake_block, snake_list):
    for segment in snake_list:
        pygame.draw.circle(screen, green, (segment[0] + snake_block // 2, segment[1] + snake_block // 2), snake_block // 2)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [width / 6, height / 3])

def place_food(snake_List):
    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
    while [foodx, foody] in snake_List:
        foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
    return foodx, foody

def gameLoop():
    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx, foody = place_food(snake_List)

    while not game_over:
        while game_close:
            screen.fill(blue)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0: 
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = snake_block
                    x1_change = 0

        # Check for wall collisions
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
            
        # Update position of the snake's head
        x1 += x1_change
        y1 += y1_change

        # Draw background image
        screen.blit(background_img, (0, 0))

        # Draw the food (red color for food)
        pygame.draw.rect(screen, red, [foodx, foody, snake_block, snake_block])

        # Create new snake head and add it to the list
        snake_Head = [x1, y1]
        snake_List.append(snake_Head)

        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Check if snake collides with itself
        for segment in snake_List[:-1]:
            if segment == snake_Head:
                game_close = True

        # Draw the snake (curved body)
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        # Check if food is eaten using a range-based check for better accuracy.
        if (x1 < foodx + snake_block and x1 + snake_block > foodx and 
            y1 < foody + snake_block and y1 + snake_block > foody):
            foodx, foody = place_food(snake_List)  
            Length_of_snake += 1

        pygame.display.update()

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Start the game loop
clock = pygame.time.Clock()  
gameLoop()
