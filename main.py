import pygame
import random
import math
from pygame import mixer
import numpy as np

#Initialize the game
pygame.init()

#Create the screen
screen = pygame.display.set_mode((800,600))

# Title and icon
pygame.display.set_caption('Pongo')
icon = pygame.image.load('racket.png')
pygame.display.set_icon(icon)
# score
score = 0
font = pygame.font.Font('freesansbold.ttf',28)
textX = 10
textY = 10
def show_score(x,y):
    scor = font.render("Score :" + str(score),True,(255,255,255))
    screen.blit(scor,(x,y))
font2 = pygame.font.Font('freesansbold.ttf',50)
def game_over():
    scor = font2.render("GAME OVER",True,(255,255,255))
    screen.blit(scor,(280,250))
#player
player_height = 15
player_width = 120
playerX = 400-player_width/2
playerY = 550
playerX_change = 0
playerY_change = 0
gameloop = 1
#Ball
ballX = 400
ballY = 150
ball_radius = 10
ballX_change = 0.5
ballY_change = 0.5
signX = 1
signY = 1


def player(screen,playerX,playerY):
    global player_height
    global player_width
    pygame.draw.rect(screen,(255,255,255),(playerX,playerY,player_width,player_height))

def ball(screen,ballX,ballY):
    global ball_radius
    pygame.draw.circle(screen,(255,255,255),(ballX,ballY),ball_radius)




running = True
while running:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #if keystoke is pressed check whether it's right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -1
            if event.key == pygame.K_RIGHT:
                playerX_change = 1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                playerX_change = 0
# Player Movement
    playerX = playerX + playerX_change
    playerY = playerY + playerY_change
    if playerX < 0:
        playerX = 0
    if playerX > 800-player_width:
        playerX = 800-player_width

# Ball Movement
    ballX = ballX + signX*ballX_change
    ballY = ballY + signY*ballY_change
    if ballX > 800-ball_radius:
        signX = -1*signX
    if ballX < 0+ball_radius:
        signX = -1*signX
    if ballY < 0+ball_radius:
        signY = -1*signY

    if ballY == playerY and ballX>playerX and ballX<playerX+player_width:
        signY = -1*signY
        score = score+1
        ballX_change = 1.05*ballX_change
        ballY_change = 1.05*ballY_change

    if ballY > 620:
        game_over()


    player(screen,playerX,playerY)
    ball(screen,round(ballX),round(ballY))
    show_score(textX,textY)
    if gameloop ==1 :
        pygame.time.delay(3000)
        gameloop = gameloop+1
    pygame.display.update()
