import pygame
import time
import random

pygame.font.init()

WIDTH,HEIGHT = 1100,600

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Swastik's Game")


def intro():
    WIN = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("Swastik's Game")
    clock = pygame.time.Clock()
    WIN.fill(harbor)
    
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            key_press = pygame.key.get_pressed()
            if key_press[pygame.K_SPACE]:

                run = False
        WIN.fill(harbor)

        fontest = pygame.font.Font("freesansbold.ttf", 30)
        text = fontest.render("Hello Everyone, This is a basic ping pong game developed with Pygame.",False,white)
        WIN.blit(text,(5,20))
        text2 = fontest.render("Tutorial",False,black)
        WIN.blit(text2,(5,100))
        font2 = pygame.font.Font("freesansbold.ttf", 25)
        text3 = font2.render("This is a multiplayer game played on the same computer.",False,white)
        WIN.blit(text3,(5,200))
        text4 = font2.render("The person seated on the left can control the bat with the (w) and (s) keys AND ",False, white)
        WIN.blit(text4,(5,250))    
        text5 = font2.render("the one on the right can control it with the arrow buttons.",False,white)
        WIN.blit(text5,(5,300))
        text6 = font2.render("Press the ( SPACE ) BUTTON to play ....  ENJOY !!! ",False,black)
        WIN.blit(text6,(5,370))


        pygame.display.update()
    
    timer()


def timer():
    WIN = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("Swastik's Game")
    clock = pygame.time.Clock()
    
    run = True
    while run:
        WIN.fill(harbor)
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        global text
        for i in range (3,-1,-1):
            text1 = i
            fontest = pygame.font.Font("freesansbold.ttf", 200)
            text = fontest.render(str(text1),False,white)
            WIN.blit(text,(450,200))
            pygame.display.update()
            time.sleep(1)
            WIN.fill(harbor)
            
        run = False
    main()

            
    


signs = ["+","-"]
white = (255,255,255)
harbor = (85,102,153)
black = (0,0,0)
FPS = 60
ball_speed_x,ball_speed_y= int(random.choice(signs) +"6"), int(random.choice(signs)+"6")
size = (10,110)
border = pygame.Rect((WIDTH/2)-5,0,2,HEIGHT)
left_score = 0
right_score = 0
gamefont = pygame.font.Font("freesansbold.ttf", 32)


def draw_window(left,right,ball,left_text,right_text):
    WIN.fill(harbor)
    pygame.draw.circle(WIN,white,(WIDTH/2,HEIGHT/2),100)
    pygame.draw.circle(WIN,harbor,(WIDTH/2,HEIGHT/2),95)
    pygame.draw.rect(WIN,white,border)
    pygame.draw.ellipse(WIN,white,ball)
    pygame.draw.rect(WIN,white,left)
    pygame.draw.rect(WIN,white,right)
    WIN.blit(left_text,(WIDTH/2-50,HEIGHT/2-15))
    WIN.blit(right_text,(WIDTH/2+25,HEIGHT/2-15))
    
    pygame.display.update()

def movement(red,yellow,key_press):
    # if key_press[pygame.K_a] and yellow.x-5 > 0:
    #     yellow.x-=5
    # if key_press[pygame.K_d] and yellow.x + yellow.width + 5 < border.x:
    #     yellow.x+=5
    if key_press[pygame.K_w] and yellow.y-5 > 0:
        yellow.y-=5
    if key_press[pygame.K_s] and yellow.y + size[1] + 5 < HEIGHT:
        yellow.y+=5

    # if key_press[pygame.K_LEFT] and red.x - 5 > border.x + border.width:
    #     red.x-=5
    # if key_press[pygame.K_RIGHT] and red.x + size[0] +5 < WIDTH:
    #      red.x+=5
    if key_press[pygame.K_UP] and red.y - 5 > 0:
        red.y-=5
    if key_press[pygame.K_DOWN] and red.y + size[1] +5 < HEIGHT:
        red.y+=5


# def bullet(red,yellow,key_press):
#     if key_press[pygame.K_LCTRL] and len(YELLOW_BULLETS) < MAX_BULLETS:
#         bullet = pygame.Rect(yellow.x + shipsize[0], yellow.y + shipsize[1]/2, 5,5 )
#         YELLOW_BULLETS.append(bullet)

#     if key_press[pygame.K_RCTRL] and len(RED_BULLETS) < MAX_BULLETS:
#         bullet = pygame.Rect(red.x , red.y + shipsize[1]/2, 5,5 )
#         RED_BULLETS.append(bullet)


def check_collision(ball,right,left):
    global left_score
    global right_score
    global ball_speed_x
    global ball_speed_y
    if ball.x <= 0 :
        ball.x = WIDTH/2-10
        ball.y = HEIGHT/2
        right_score+=1
        time.sleep(1)


    if ball.x >= WIDTH :
        ball.x = WIDTH/2-10
        ball.y = HEIGHT/2
        left_score+=1
        time.sleep(1)

    
    if ball.y == 0 or ball.y == HEIGHT:
        ball_speed_y *=-1 

    if left.colliderect(ball):
        ball_speed_x *= -1
    if right.colliderect(ball):
        ball_speed_x *= -1






def main():
    right = pygame.Rect(WIDTH - size[0],HEIGHT/2 - size[1]/2 ,size[0],size[1])
    left = pygame.Rect(0,HEIGHT/2 - size[1]/2,size[0],size[1])
    ball = pygame.Rect(WIDTH/2-12,HEIGHT/2,12,12)
     
    clock = pygame.time.Clock()

    run = True
    time.sleep(1)
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        ball.x+=ball_speed_x
        ball.y-=ball_speed_y

        check_collision(ball,right,left)      
        left_text = gamefont.render(str(left_score),False,white)
        right_text = gamefont.render(str(right_score),False,white)  
        
        key_press = pygame.key.get_pressed()
        movement(right,left,key_press)
        draw_window(right,left,ball,left_text,right_text)
        
    pygame.quit()


if __name__ == "__main__":
    intro()

