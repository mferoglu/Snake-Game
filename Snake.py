import pygame
import sys
import pyautogui


WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
blockSize = 20
rowBlockNumber = int(WINDOW_WIDTH/blockSize)
columnBlockNumber = int(WINDOW_HEIGHT/blockSize)

def createGrid(gridView):
    for x in range(rowBlockNumber):
        gridView.append([])
        for y in range(columnBlockNumber):
            print(x)
            rect = pygame.Rect(x*blockSize,y*blockSize,blockSize,blockSize)
            gridView[x].append(rect)




def drawGrid(grid,bx,by):
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            rect = grid[x][y]
            cursor = pygame.mouse.get_pos()
            #if cursor[0] > x*blockSize and cursor[0] < x*blockSize+blockSize and cursor[1] > y*blockSize and cursor[1] < y*blockSize+blockSize :
            if x == bx and y == by:
                pygame.draw.rect(SCREEN,(0, 0, 0),rect,0)
            else:
                pygame.draw.rect(SCREEN,(255, 0, 0),rect,0)


def directionCheck(direction,currentx,currenty):
    x = 0
    y = 0

    if direction == "right":
            x = currentx + 1
            if x == rowBlockNumber:
                x = 0
            y = currenty
    if direction == "left":
            x = currentx - 1
            if x == -1:
                x = rowBlockNumber-1
            y = currenty
    if direction == "up":
            y = currenty - 1
            if y == - 1:
                y = columnBlockNumber-1
            x = currentx
    if direction == "down":
            y = currenty + 1
            if y == columnBlockNumber:
                y = 0
            x = currentx
    return (x,y)


def main():
    global SCREEN,CLOCK
    grid = []
    currentx = 0
    currenty = 0
    nextblockx = 0
    nextblocky = 0
    direction = "right"
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_HEIGHT,WINDOW_WIDTH))
    CLOCK = pygame.time.Clock()
    createGrid(grid)
    #SCREEN.fill((0,0,0))
    while True:
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            direction = "right"
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            direction = "left"
        if pygame.key.get_pressed()[pygame.K_UP]:
            direction = "up"
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            direction = "down"

        point = directionCheck(direction,currentx,currenty)
        nextblockx = point[0]
        nextblocky = point[1]

        CLOCK.tick(10)
        drawGrid(grid,nextblockx,nextblocky)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        currentx = nextblockx
        currenty = nextblocky


main()