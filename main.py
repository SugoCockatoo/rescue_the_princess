import pygame 
import time
import random 
from utils import *

pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((720, 480))
pygame.display.set_caption("Rescue the Princess")
WHITE = (255, 255, 255)
alien_list = []
pygame.font.init()
font = pygame.font.Font(None, 36) #Thxxx

king_img = "images/cockatiel_img.png"
princess_img = "images/seeds_img.png"
monster_img = "images/balloon_img.png"
bomb_img = "images/needle_img.png"
won_img = "images/you_win.png"
won_img = "images/you_lose.png"

background_image = pygame.image.load("images/backround.jpg").convert()
background_image = pygame.transform.scale(background_image, (720, 480))

bird = Player(10, 20, king_img, 5, )
bird.reset(window)

balloon = Enemy(200, 200, monster_img, 2)
balloon.reset(window)

wall_parameters = [
    {"x":0, "y":100, "width":10, "height":350}
]
walls = list()
for wall in wall_parameters:
    new_wall = Wall(wall["x"], wall["y"], WHITE, wall["width"], wall["height"])
    new_wall.draw(window)
    walls.append(new_wall)

while True:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
    window.blit(background_image, (0, 0))
    text = font.render("Frame Rate: " + str(int(clock.get_fps())), 1, (255, 255, 255)) # For testing :D
    window.blit(text, (10, 20))
    for wall in walls:
        wall.draw(window)
    bird.reset(window)
    bird.move(walls)
    balloon.reset(window)
    balloon.catch(window)
    pygame.display.update()
    clock.tick(60) 