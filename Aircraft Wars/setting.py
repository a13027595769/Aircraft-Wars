class Settings():
    def __init__(self):
        """初始化游戏的设置"""
        #屏幕设置
        self.screen_width = 700
        self.screen_height= 400
        self.bg_color=(230,230,230)
        #速度设置
        self.ship_speed_factor = 1.5
        self.ship_limit = 3
        #子弹设置
        self.bullet_speed_factor = 3
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=60,60,60
        self.bullets_allowed = 3
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        #fleef_direction = 1 表示向右走，-1就是向左走
        self.fleet_direction = 1

        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.fleet_direction = 1

        def increase_speed(self): """提高速度设置"""

    def increase_speed(self):
        """提高速度设置"""

        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
