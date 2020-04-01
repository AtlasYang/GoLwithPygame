import pygame
import sys, random
from pygame.locals import *

pygame.init()

WIDTH = int(input('Input width(720~1080p recommended): '))
HEIGHT = int(input('Input height(480~720p recommended): '))
LEN = int(input('Input cell size(5~20p recommended): '))
print('Tab space to process 1 step. Have fun!')

DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Life Game')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)                               
BLUE = (0, 0, 255)
SKYBLUE = (0, 128,128)

cellMap = []
posMap = []
for i in range(int((WIDTH/LEN)*(HEIGHT/LEN))):
    cellMap.append(0)
for j in range(0, HEIGHT, LEN):
    for i in range(0, WIDTH, LEN):
        posMap.append([i, j])

def draw_sq(pos):
    recta = (pos[0], pos[1], LEN, LEN)
    pygame.draw.rect(DISPLAYSURF, BLUE, recta)

def draw_edgeline():
    for i in range(0, WIDTH+LEN, LEN):
        pygame.draw.line(DISPLAYSURF, SKYBLUE, (i, 0), (i, HEIGHT))
    for j in range(0, HEIGHT+LEN, LEN):
        pygame.draw.line(DISPLAYSURF, SKYBLUE, (0, j), (WIDTH, j))

t = []
def process():
    global cellMap, t
    for i in range(len(cellMap)):
        try:
            s = cellMap[i-int(WIDTH/LEN) + 1] + cellMap[i-int(WIDTH/LEN)] + cellMap[i-int(WIDTH/LEN)-1] + cellMap[i-1] + cellMap[i+1] + cellMap[i+int(WIDTH/LEN)+1] + cellMap[i+int(WIDTH/LEN)] + cellMap[i+int(WIDTH/LEN)-1]
            if s<=1 or s>=4:
                t.append(0)
            elif s == 3:
                t.append(1)
            else:
                t.append(cellMap[i])
        except:
            t.append(cellMap[i])
            
    cellMap = t
    t = []
    return

def graphize():
    for i in range(len(cellMap)):
        if cellMap[i] == 1:
            draw_sq(posMap[i])

pos = [-1, -1]
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            pos = list(event.pos)
            for i in range(len(posMap)):
                if pos[0]  < posMap[i][0]:
                    pos[0] = posMap[i-1][0]
                    break
            for i in range(len(posMap)):
                if pos[1] < posMap[i][1]:
                    pos[1] = posMap[i-int((WIDTH/LEN))][1]
                    break
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                process() 
                DISPLAYSURF.fill(BLACK)
                draw_edgeline()
                graphize()
                draw_edgeline()
                pygame.display.update()

    index = -1
    for j in range(len(posMap)):
	    if posMap[j] == pos:
    		index = j


    if not index == -1:
            if cellMap[index] == 1:
                cellMap[index] = 0
            else:
                cellMap[index] = 1
            pos = [-1, -1]
            index = -1
  
    DISPLAYSURF.fill(BLACK)
    draw_edgeline()
    graphize()
    draw_edgeline()
    pygame.display.update()
    
        
            
