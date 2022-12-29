# made by mr.jay kumar 
import pygame
import random
import os

pygame.init()
#colour
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
snakegreen = (35, 45, 40)
#background image
bgimg = pygame.image.load('backgroundpic.jpg')
intro = pygame.image.load('intropic.jpg')
# outro = pygame.image.load('backgroundpic.jpg')
# Creating a window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width , screen_height))

#game title
pygame.display.set_caption("Snake the Game")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None ,55)

def text_screen(text , colour, x , y):
    screen_text = font.render(text , True ,colour)
    gameWindow.blit(screen_text , [ x,y ])
def plot_snake(gameWindow , color  ,snk_list ,snake_size  ):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [ x , y , snake_size , snake_size])

def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.blit(intro,(0,0))

        # text_screen("Welcome to Snake Game", black, 240, 100)
        text_screen("Press space bar to play ", white, 240, 95)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # adding song
                    pygame.mixer.init()
                    pygame.mixer.music.load('../snakesongbackground.mp3')
                    pygame.mixer.music.play()
                    gameloop()

        pygame.display.update()
        clock.tick(60)

#-----------game loop------------------------------
def gameloop():
#game loops variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1

#-------------making high score program ----------------
    if(not os.path.exists("highscore.txt")):
        with open("highscore.txt", "w")as f:
            f.write("0")
    with open("highscore.txt", "r") as f:
        highscore = f.read()


    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_height / 2)
    score = 0
    init_velocity = 5
    snake_size = 30
    fps = 60
##--------game over screen-----------
    while not exit_game:
        if game_over:
            with open("highscore.txt", "w")as f:
                f.write(str(highscore))

            gameWindow.fill(snakegreen)
            # gameWindow.blit(outro,(0,0))
            text_screen("Game over ! Press Enter to continue ", white, 200,300)
            text_screen("Score:" + str(score), red , 385, 350)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()


        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_q:
                        score += 5

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y


            if abs(snake_x - food_x)<15 and abs(snake_y - food_y)<15:
                score +=10

                food_x = random.randint(20, screen_width/2)
                food_y = random.randint(20  , screen_height/2)
                snk_length +=5
                if score>int(highscore):
                    highscore = score

            gameWindow.blit(bgimg,(0,0))
            text_screen("Score :" + str(score )+ " Highscore : " + str(highscore), red, 5,5)
            pygame.draw.rect(gameWindow , red ,[food_x , food_y , snake_size , snake_size])
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]
            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.init()
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
                pygame.mixer.init()
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()


            plot_snake(gameWindow,black, snk_list , snake_size)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()


welcome()

