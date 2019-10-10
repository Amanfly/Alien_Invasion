class Settings():
    """A class to store all the elements pf allien Invaison"""
    def __init__(self):
        """Intiliaze the game settings"""
        #Screen Settings
        self.screen_width=1000
        self.screen_height=600
        self.bg_color=(230,230,230)
        # Ship Setting
        self.ship_speed_factor=1.5
        self.ship_limit=3
        #Bullet Setting
        self.bullet_speed_factor=1
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=(60,60,60)
        self.bullets_allowed=3
        self.alien_speed_factor=1

        self.fleet_drop_speed=10
        # fleet_direction of 1 represents right;-1 represents left
        self.fleet_direction=1