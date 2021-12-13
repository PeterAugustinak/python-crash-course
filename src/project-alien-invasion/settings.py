"""Module with settings for the game"""


class Settings:
    """A clas to store all settings for Alien Invasion game"""

    def __init__(self):
        """Initialize the game settings"""
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # ship settings
        self.ship_limit = 3
        self.ship_speed = 1.5

        # bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 100
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # alien setting
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet direction: 1 = right, -1 = left
        self.fleet_direction = 1

