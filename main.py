'''
you will need to install:
pygame
math
random
'''

import pygame
from pygame.locals import *
import random
from character_class_v2 import Character
#from Enemy import enemy

# Intialize pygame
pygame.init()

WHITE = (255, 255, 255)
screen = pygame.display.set_mode((800, 600))

########################################################################################
# Players data
playerX = 400
playerY = 300
playerX_change = 0
playerY_change = 0



# Enemies data
Enemy_list = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
rect_lst = []
num_of_enemies = 6
mx, my = pygame.mouse.get_pos()

# Player object
character = Character(playerX,playerY,playerX_change,playerY_change,mx,my)


# Entity groups
#print(zombie)
# for i in range (num_of_enemies):
#     Enemy_list.append(enemy(rect_lst))


# zombie_group = pygame.sprite.Group()#
# zombie_group.add(enemy(Enemy_list, enemyX, enemyY, enemyX_change, enemyY_change,rect_lst))


def collision():
    pass


running = True


# -------- Main Program Loop -----------
def main():
    while running:
        # Background colour
        screen.fill(WHITE)

        # Adding the exit button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            # Fire button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                   character.fire()

        # Enemy loop
        # for i in range(num_of_enemies): # Loops throw enemies and draws them
        #     zombie.draw(i, enemyX[i], enemyY[i])
        #     zombie.move_to_player(character.X, character.Y)


        # Bullet list
        for bullet in character.bullets:
            bullet.move()
            bullet.draw(screen)

        #]for bullet in character.bullets:



        # collide = character.rect.colliderect(rect2)

        #zombie.update()
        character.update()
        pygame.display.update()



# Calling main program
main()
