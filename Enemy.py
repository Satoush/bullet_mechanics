import pygame
import random

screen = pygame.display.set_mode((800, 600))


class enemy():
    def __init__(self, rect_lst):
        super().__init__()
        self.Image_path = pygame.image.load('Assets/zombie.png')
        self.X = random.randint(0, 725)
        self.Y = random.randint(0, 600)
        self.changeX = changeX
        self.changeY = changeY
        self.velocity = 0.01
        self.num_of_enemies = 6
        self.rect = self.Image_path.get_rect(center = (random.randint (0,725),(random.randint(0,600))))
        self.rect_lst = rect_lst




    def draw(self, X, Y):
        screen.blit(self.Image_path, (X, Y))
        #pygame.draw.rect(screen, pygame.Color("red"), (self.rect))

    # Enemies are put onto a list and
    def adding_multiple_enemies(self):



    # Adding basic movement towards player
    def move_to_player(self, PlayerX,PlayerY):
        if self.X > PlayerX:
            self.changeX =  -1 * self.velocity

        elif self.X < PlayerX:
            self.changeX = self.velocity

        else:
            if self.Y == PlayerX:
                self.changeX = 0


        if self.Y > PlayerY:
            self.changeY =  -1 * self.velocity

        elif self.Y < PlayerY:
            self.changeY = self.velocity

        else:
            if self.Y == PlayerY:
                self.changeY = 0



        self.X += self.changeX
        self.Y += self.changeY

            # self.rect[1] += self.changeY
            # self.rect[0] += self.changeX

    


    def update(self):
        pygame.draw.rect(screen, pygame.Color("red"), (self.rect))



""""
        dirvect = pygame.math.Vector2(PlayerX - self.x,
                                      player.rect.y - self.rect.y)
        dirvect.normalize()
        # Move along this normalized vector towards the player at current speed.
        dirvect.scale_to_length(self.speed)
        self.rect.move_ip(dirvect)
"""

"""

"""
# def move_to_player(self,playerX,playerY):
#    for i in range (self.num_of_enemies):
#       if self.X >= playerX:
