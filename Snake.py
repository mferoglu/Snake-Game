import pygame
import sys
import pyautogui


WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600





def drawGrid():
    blockSize = 20
    for x in range(WINDOW_WIDTH):
        for y in range(WINDOW_HEIGHT):
            rect = pygame.Rect(x*blockSize,y*blockSize,blockSize,blockSize)
            cursor = pyautogui.position()
            if cursor[0] > x*blockSize and cursor[0] < x*blockSize+blockSize and cursor[1] > y*blockSize and cursor[1] < y*blockSize+blockSize :
                pygame.Surface.fill(pygame.Color("blue"),rect)
            
            pygame.draw.rect(SCREEN,(255, 0, 0),rect,0)


def main():
    global SCREEN,CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_HEIGHT,WINDOW_WIDTH))
    CLOCK = pygame.time.Clock()
    #SCREEN.fill((0,0,0))
    while True:
        drawGrid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


main()