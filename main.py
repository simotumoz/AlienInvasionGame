#In Alien Invasion, the player controls a ship that appears at
#the bottom center of the screen. The player can move the ship
#right and left using the arrow keys and shoot bullets using the
#spacebar. When the game begins, a fleet of aliens fills the sky
#and moves across and down the screen. The player shoots and
#destroys the aliens. If the player shoots all the aliens, a new fleet
#appears that moves faster than the previous fleet. If any alien hits
#the player’s ship or reaches the bottom of the screen, the player
#loses a ship. If the player loses three ships, the game ends.

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():

    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    play_button = Button(ai_settings, screen, "Play now")

    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    ship = Ship(ai_settings, screen)
    bullets = Group() 

    alien = Alien(ai_settings, screen)
    aliens = Group()

    gf.create_fleet(ai_settings, screen, ship, aliens)

    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:

            ship.update()
            bullets.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)
        
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)


if __name__ == "__main__":
    run_game()
