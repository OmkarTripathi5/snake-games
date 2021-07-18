import pygame
import random

pygame.init()
screen_width = 550
screen_height = 500
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)


font= pygame.font.Font(None,50)
def plot_snake(place,color,snk_list,snakesize):

    for x,y in snk_list:
        pygame.draw.rect(place, color, [x, y, snakesize, snakesize])

def text_screen(text,color,x,y):
    screen_score = font.render(text,True,color)
    gamewindow.blit(screen_score,[x,y])
gamewindow = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()
pygame.display.set_caption("SnakewithOmkar")
pygame.display.update()
def welcome():
    exit_game = False
    fps = 45
    while not exit_game:
        gamewindow.fill(white)
        text_screen("Welcome In Snake Game",black,95,150)
        text_screen("Press Space Bar to Start Game",black,35,200)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game()
        pygame.display.update()
        clock.tick(fps)

def game():
    exit_game = False
    over_game = False
    snake_x = 34
    snake_y = 20
    snake_size = 15
    initvelocity = 5
    food_x = random.randint(5, 480)
    food_y = random.randint(5, 480)
    food_size = 10
    fps = 60
    snk_list = []
    music = pygame.mixer.Sound("song1.mp3")

    velocity_x = 0
    velocity_y = 0

    score = 0
    snake_length = 1

    while not exit_game:
        if over_game:
            gamewindow.fill(white)
            pygame.display.update()
            text_screen("Game Over Press Enter",red,100,250)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = initvelocity
                        velocity_y = 0

                    elif event.key == pygame.K_LEFT:
                        velocity_x = -initvelocity
                        velocity_y = 0

                    elif event.key == pygame.K_UP:
                        velocity_y = -initvelocity
                        velocity_x = 0

                    elif event.key == pygame.K_DOWN:
                        velocity_y = initvelocity
                        velocity_x = 0


            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y
            gamewindow.fill(white)

            pygame.draw.rect(gamewindow,red,[food_x,food_y,food_size,food_size])

            plot_snake(gamewindow, black, snk_list, snake_size)
            text_screen("Score:" + str(score), red, 350, 5)


            if (abs(snake_x - food_x)<6) and (abs(snake_y-food_y)<6):
                score += 5

                food_x = random.randint(5,480)
                food_y = random.randint(5,480)
                snake_length +=5
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snake_length:
                del snk_list[0]
            if head in snk_list[:-1]:
                over_game = True

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                over_game = True



        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()


welcome()