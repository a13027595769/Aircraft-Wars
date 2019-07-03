import sys
import pygame
from setting import Settings
from ship import Ship
import game_function as gf
from alien import Alien
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
def run_game():
    #初始化游戏并且创建一个游戏对象
    pygame.init()
    #初始化屏幕宽高颜色
    ai_setting = Settings()

    screen  =pygame.display.set_mode((ai_setting.screen_width,ai_setting.screen_width))
    pygame.display.set_caption("Alien Invasion")
    #创建play按钮
    play_button = Button(ai_setting,screen,"Play")
    stats = GameStats(ai_setting)
    # bg_color = {230,230,230}
    #创建一个ship的实例，在while前面，避免创建很多飞船
    ship = Ship(ai_setting,screen)
    #创建一个用于存储子弹的编组
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_setting,screen,ship,aliens)
    alien = Alien(ai_setting,screen)
    pygame.display.flip()
    #开始游戏的主循环
    while True:
        #监听键盘和鼠标事件
        gf.check_events(ai_setting,screen,stats,play_button,ship,aliens,bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_setting,screen,ship,aliens,bullets)
            gf.update_aliens(ai_setting,stats,screen,ship,aliens,bullets)
        gf.update_screen(ai_setting,screen,stats,ship,aliens,bullets,play_button)

run_game()