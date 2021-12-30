import pygame
import math

screen = pygame.display.set_mode((800, 600))


class bullet():
    def __init__(self,Image_path,colour ,pos_X, pos_Y,velocity,mx,my):
        self.Image_path = Image_path
        self.image = pygame.image.load(Image_path)
        self.rect = self.image.get_rect(center=(400, 300))
        self.colour = colour
        self.posX = pos_X
        self.posY = pos_Y
        self.velocity = velocity
        ##################################################
        angle = math.atan2(my - pos_Y, mx - pos_X)
        self.dx = math.cos(angle) * velocity
        self.dy = math.sin(angle) * velocity
       # players x and


    def move(self):
        self.posX += self.dx
        self.posY += self.dy
        self.rect.x = int(self.posX)
        self.rect.y = int(self.posY)


    def draw(self, surface):
        pygame.draw.rect(surface, self.colour, self.rect)

    def destroy(self,bullet_array):
        bullet_array.remove(self)
        del self



    def update(self):
        #self.move()
        self.destroy()














