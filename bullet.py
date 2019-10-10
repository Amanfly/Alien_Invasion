import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    """A class to manage the bullet fire from the ship"""
    def __init__(self,ai_settings,screen,ship):
        """Create a bullet object at ship's curent location"""
        super(Bullet,self).__init__()
        self.screen=screen
        # Create a bullet rect at(0,0) and then set positions
        self.rect= pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx=ship.rect.centerx
        self.rect.top=ship.rect.top
        # store the bullet's position in decimal value
        self.y=float(self.rect.y)
        self.color=ai_settings.bullet_color
        self.speed_factor=ai_settings.bullet_speed_factor
    def update(self):
        """Move the bullet up the screen"""
        #update the decimal place of the bullet
        self.y-=self.speed_factor
        #update the rect position
        self.rect.y=self.y
    def draw_bullet(self):
        """Draw the bullet to the screen"""
        pygame.draw.rect(self.screen,self.color,self.rect)






