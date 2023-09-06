class Settings:
    """A class to store all settings for Rocket Game."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (40, 160, 200)

        # Rocket settings
        self.rocket_speed = 10  # Using a float to give finer control
