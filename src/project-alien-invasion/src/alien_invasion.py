# standard library imports
import sys
from time import sleep
# external library import
import pygame
import pygame.mixer
# local library imports
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien
from sounds import Sounds

class ALienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        # create an instance to store game statistics
        self.stats = GameStats(self)
        self.scoreboard = Scoreboard(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        # make Play button
        self.play_button = Button(self, "Play")
        # initialize sounds instance
        self.sounds = Sounds()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()

    def _check_events(self):
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # 14-5
                self._save_high_score()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    # 14-1
    def _start_game(self):
        """Starts game if mouse click on Play button or p key is pressed"""
        # reset game statistics
        self.settings.initialize_dynamic_settings()
        self.stats.reset_stats()
        self.stats.game_active = True
        self.scoreboard.prep_images()

        # get rid of any remaining aliens and bullets
        self.aliens.empty()
        self.bullets.empty()

        # create a new fleet and center the ship
        self._create_fleet()
        self.ship.center_ship()

        # hide the mouse cursor
        pygame.mouse.set_visible(False)

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # 14-1
            self._start_game()

    def _check_keydown_events(self, event):
        """Respond to key presses"""
        if event.key == pygame.K_RIGHT:
            # Move the ship to the right
            self.ship.moving_right = True
        if event.key == pygame.K_LEFT:
            # Move the ship to the right
            self.ship.moving_left = True
        if event.key == pygame.K_q:
            # 14-5
            self._save_high_score()
            sys.exit()
        if event.key == pygame.K_SPACE:
            self._fire_bullet()
        # 14-1
        if event.key == pygame.K_p:
            if not self.stats.game_active:
                self._start_game()

    def _check_keyup_events(self, event):
        """Response to ey releases"""
        # stop moving ship when key is released
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    # 14-5
    def _save_high_score(self):
        """Save current high score to the file before exit the game"""
        with open("highscore.txt", "w") as f:
            f.write(str(self.stats.high_score))

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of all bullets."""
        # update bullet positions
        self.bullets.update()

        # get rid of the bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Respond to the bullet-alien collisions."""
        # check for any bullets that have hit aliens
        # if so, ghet rid of the bullet and the alien
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True
        )

        if collisions:
            self.sounds.explosion.play()
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.scoreboard.prep_score()
            self.scoreboard.check_high_score()

        if not self.aliens:
            # 14-6
            self._start_new_level()

    # 14-6
    def _start_new_level(self):
        """When all aliens fleet is destroyed, start new level."""
        # destroy existing bullets and create new fleet
        self.bullets.empty()
        self._create_fleet()
        self.settings.increase_speed()

        # increase level
        self.stats.level += 1
        self.scoreboard.prep_level()

    def _update_aliens(self):
        """
        Check if the fleet is at an edge, then update the position of
        all aliens in the fleet.
        """
        self._check_fleet_edges()
        self.aliens.update()

        # look for alien-ship collisions.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # look for aliens hit the bottom
        self._check_aliens_bottom()

    def _ship_hit(self):
        """Respond to the ship being hit by alien."""
        if self.stats.ships_left > 0:
            # decrement ships left and update scoreboard
            self.stats.ships_left -= 1
            self.scoreboard.prep_ships()

            # get rid of any remaining aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            # create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()

            # pause
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Make an alien
        alien = Alien(self)

        # determine the numbers of alien that fits on the row
        alien_width, alien_height = alien.rect.width, alien.rect.height
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_of_aliens_in_row = available_space_x // (2 * alien_width)

        # determine the number of rows of aliens that fit on the screen
        ship_height = self.ship.rect.height
        available_space_row = (self.settings.screen_height -
                                  (3 * alien_height) - (2 * ship_height))
        number_of_rows = available_space_row // (2 * alien_height)

        # create full fleet of aliens
        for row_number in range(number_of_rows):
            for alien_number in range(number_of_aliens_in_row):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """Create an alien and place it in the row."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.width, alien.rect.height
        alien.x = alien_width + (2 * alien_width * alien_number)
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + (2 * alien.rect.height * row_number)
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached the edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_aliens_bottom(self):
        """Check if any aliens have reach the bottom of the screen."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # treat this the same as ship got hit
                self._ship_hit()
                break

    def _update_screen(self):
        # redraw the screen during each pass through the loop
        self.screen.fill(self.settings.background)
        # self.screen.blit(self.settings.background, (0, 0))
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        # draw the score information
        self.scoreboard.show_score()

        # draw the Play button if the game is inactive
        if not self.stats.game_active:
            self.play_button.draw_button()
        # Make the most recently drawn screen visible
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance and run the game
    ai = ALienInvasion()
    ai.run_game()
