import pygame

pygame.init()

screen= pygame.display.set.mode((800,600))
pygame.display.set_caption("Shooting Game")

class Player():
    def_init_(self):
    super()._init_()
    self.image = pygame.Surface((5,50))
    self.image.fill((225,255,255))
    self.rect = self.image.get



running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT
        running = False

pygame.quit()