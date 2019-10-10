import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from game_stats import GameStats
from alien import Alien
from button import Button
import game_functions as gf


def run_game():
    """Intiliaze  Game and screen object"""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make the Play Button
    play_button=Button(ai_settings,screen,"Play")

    # Create an instance to store statistics
    stats=GameStats(ai_settings)

    # Make a Ship
    ship = Ship(ai_settings, screen)

    # Make a group to store values
    bullets = Group()
    aliens=Group()

    gf.create_fleet(ai_settings,screen,ship,aliens)

    # Start the main loop for the game
    while True:
        gf.check_events(ai_settings, screen,stats,play_button, ship, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,ship,aliens,bullets)
            gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)

        gf.update_screen(ai_settings, screen,stats, ship, aliens, bullets,play_button)

run_game()
