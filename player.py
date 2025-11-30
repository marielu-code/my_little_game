import pygame
from game_object import GameObject
from settings import Properties
from resources import RESOURCES, Animation

class Player(GameObject, Properties):
    def __init__(self, x, y, *args, **kwargs):
        super().__init__(x=x, y=y, *args, **kwargs)
        self.idle_anim = Animation(RESOURCES['Player_Idle'], speed = 7)
        self.walk_anim = Animation(RESOURCES['Player_Walk'], speed = 5)
        self.current_animation = self.idle_anim
        super().__init__(x=x, y=y, *args, **kwargs)
        self.image = pygame.Surface((32,32))
        self.image.fill((255,0,0))
        self.image = self.current_animation.get_current_frame()
        self.rect = self.image.get_rect(topleft=(x, y))
        self.is_moving = False
    def handle_input(self):
        pass
    def update(self):
        """if self.is_moving:
            self.current_animation = self.walk_animation
        else:
            self.current_animation = self.idle_animation
        pass"""

        self.current_animation.update()
        self.image = self.current_animation.get_current_frame()
