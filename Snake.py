import pygame
import sys
import pyautogui
import random
import os
pygame.font.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
blockSize = 20
rowBlockNumber = int(WINDOW_WIDTH/blockSize)
columnBlockNumber = int(WINDOW_HEIGHT/blockSize)

def createGrid(gridView):
    for x in range(rowBlockNumber):
        gridView.append([])
        for y in range(columnBlockNumber):
            rect = pygame.Rect(x*blockSize,y*blockSize,blockSize,blockSize)
            gridView[x].append(rect)




def drawGrid(grid,nextblock,bait):
    global EATEN
    EATEN = False

    for x in range(len(grid)):
        for y in range(len(grid[x])):
            rect = grid[x][y]

            if x == nextblock[0] and y == nextblock[1]:
                pygame.draw.rect(SCREEN,(0, 0, 0),rect,0)
            elif x == bait[0] and y == bait[1]:
                pygame.draw.rect(SCREEN,(43, 0, 255),rect,0)
            else:
                pygame.draw.rect(SCREEN,(255, 0, 0),rect,0)


def directionCheck(direction,currentblock):
    x = 0
    y = 0

    if direction == "right":
            x = currentblock[0] + 1
            if x == rowBlockNumber:
                x = 0
            y = currentblock[1]
    if direction == "left":
            x = currentblock[0] - 1
            if x == -1:
                x = rowBlockNumber-1
            y = currentblock[1]
    if direction == "up":
            y = currentblock[1] - 1
            if y == - 1:
                y = columnBlockNumber-1
            x = currentblock[0]
    if direction == "down":
            y = currentblock[1] + 1
            if y == columnBlockNumber:
                y = 0
            x = currentblock[0]
    return (x,y)

def createBait():
    bait = [0,0]
    bait[0] = random.randint(0,rowBlockNumber-1)
    bait[1] = random.randint(0,columnBlockNumber-1)
    return bait


def main():
    global SCREEN,CLOCK,EATEN
    EATEN = False
    grid = []
    currentblock = [0 , 0]
    nextblock = [0 , 0]
    bait = [0 , 0]
    bait = createBait()

    direction = "right"
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT+100))
    CLOCK = pygame.time.Clock()
    createGrid(grid)
    #SCREEN.fill((0,0,0))
    STAT_FONT = pygame.font.SysFont("comicsans", 50)
   
    SCORE = 0
    while True:
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            direction = "right"
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            direction = "left"
        if pygame.key.get_pressed()[pygame.K_UP]:
            direction = "up"
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            direction = "down"
        
        


        point = directionCheck(direction,currentblock)
        nextblock = point

        CLOCK.tick(10)
        if EATEN:
            bait = createBait()
            SCORE += 1
        print(bait)
        SCREEN.fill((255,255,255))
        scoretext = STAT_FONT.render("SCORE : ",1,(0,0,0))
        SCREEN.blit(scoretext, (0,WINDOW_HEIGHT+10) )
        scoreNumber = STAT_FONT.render(str(SCORE),1,(0,0,0))
        SCREEN.blit(scoreNumber, (150,WINDOW_HEIGHT+10) )
        drawGrid(grid,nextblock,bait)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
      
        pygame.display.update()

        if currentblock[0] == bait[0] and currentblock[1] == bait[1]:
            EATEN = True
        currentblock = nextblock


main()