import pygame
import random 

pygame.init()
# Character Class
class Character(pygame.sprite.Sprite):
    def __init__(self, x, y, image, speed):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(image), (80, 80))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def reset(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))
    
    def collide(self, rect):
        return self.rect.colliderect(rect)

class Player(Character):
    def __init__(self, x, y, image, speed):
        super().__init__(x, y, image, speed)
        self.rebote_x = 0
        self.rebote_y = 0
    def move(self, muros):
        posicion_anterior_x = self.rect.x
        posicion_anterior_y = self.rect.y
        
        # Aplicar rebote si lo hay
        if self.rebote_x != 0 or self.rebote_y != 0:
            self.rect.x += self.rebote_x
            self.rect.y += self.rebote_y
            self.rebote_x = 0
            self.rebote_y = 0
            return
        
        # Movimiento del jugador
        keys = pygame.key.get_pressed()
        movimiento_x = 0
        movimiento_y = 0
        
        if keys[pygame.K_LEFT]:
            movimiento_x = -5
        if keys[pygame.K_RIGHT]:
            movimiento_x = 5
        if keys[pygame.K_UP]:
            movimiento_y = -5
        if keys[pygame.K_DOWN]:
            movimiento_y = 5
        
        # Intentar mover en X
        self.rect.x += movimiento_x
        colision_x = False
        for muro in muros:
            if self.rect.colliderect(muro.rect):
                colision_x = True
                # Revertir movimiento
                self.rect.x = posicion_anterior_x
                # Aplicar rebote
                self.rebote_x = -movimiento_x // 2
                break
        
        # Intentar mover en Y
        self.rect.y += movimiento_y
        colision_y = False
        for muro in muros:
            if self.rect.colliderect(muro.rect): 
                colision_y = True
                # Revertir movimiento
                self.rect.y = posicion_anterior_y
                # Aplicar rebote
                self.rebote_y = -movimiento_y // 2
                break
        
        # Mantener dentro de los límites de la pantalla
        self.rect.x = max(0, min(self.rect.x, 720 - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, 480 - self.rect.height)) 
class Wall(pygame.sprite.Sprite):
    def __init__(self, wall_x, wall_y, color, wall_height, wall_width):
        self.wall_x = wall_x
        self.wall_y = wall_y
        self.color = color 
        self.wall_height = wall_height 
        self.wall_width = wall_width
        
        self.image = pygame.Surface([wall_width, wall_height])
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
        self.image.fill(color) 
    
    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.rect.x, self.rect.y, self.wall_width, self.wall_height))

class Enemy(Character):
    def __init__(self, x, y, image, speed):
        super().__init__(x, y, image, speed)
        self.direction = 1  # 1 for down, -1 for up

    def catch(self, window):
        self.rect.x += self.direction * self.speed
        if self.rect.right >= window.get_width() or self.rect.x <= 0:
            self.direction *= -1