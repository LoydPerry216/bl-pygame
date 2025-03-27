import pygame
import sys

pygame.init()

h= 800
w= 750

screen = pygame.display.set_mode((h,w))
clock = pygame.time.Clock()
screen.fill((255,255,255))

pygame.display.set_caption("Fario")

class Player:
    def __init__(self):
        self.size = (40,60)
        self.rect = pygame.Rect((x,y), self.size)
        self.position = (100, h-125)
        self.vel =(0,0)
        self.speed = 5
        self.jump = -15
        self.gravity = 1
        self.onGround = False


    def input(self, keys):
        if keys[pygame.K_LEFT]:
            self.vel[0] = -self.speed
        elif keys[pygame.K_RIGHT]:
            self.vel[0] = self.speed
        else:
            self.vel[0] = 0           

scroll_x = 0
platforms =[
    pygame.Rect(0, h-100, 2000, 40)
    pygame.Rect(300, h-200, 200, 40)
    pygame.Rect(600, h-300, 200, 40)
    pygame.Rect(900, h-400, 200, 40)
 ]


#___________________ functions and object go above

player = Player(100, h-150)
running = True

while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit

keys = pygame.key.get_pressed()
player.input(keys) 


for plat in platforms:
    pygame.draw.rect(screen, (0,255,0), plat)

for plat in platforms:
    plat_


    pygame.display.flip()