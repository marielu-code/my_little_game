import pygame
import os
from settings import WIDTH, HEIGHT, BLACK, WHITE


class GameObject(pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
    
    def update(self):
        self.rect.x += 5
        if self.rect.left > WIDTH:
            self.rect.right = 0

class Button(pygame.sprite.Sprite):
    def __init__(self, text, x, y, WIDTH, HEIGHT, action):
        super().__init__()
        self.text = text
        self.action = action

        self.image = pygame.Surface((WIDTH, HEIGHT))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect(center=(x,y))

        self.font = pygame.font.Font(None, 36)
        self.text_surface = self.font.render(text, True, BLACK)
        self.text_rect = self.text_surface.get_rect(center=(WIDTH / 2, HEIGHT / 2))

        self.image.blit(self.text_surface, self.text_rect)
    
    def check_click(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            return self.action
        return None
        