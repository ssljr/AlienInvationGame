import pygame
import game_functions as gf
from setting import Setting
from ship import Ship
from pygame.sprite import Group


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()

    setting = Setting()
    screen = pygame.display.set_mode((setting.screen_width, setting.screen_height))
    pygame.display.set_caption('*** 外星风暴 ***')

    # 水平移动的敏捷度
    setting.ship_center_speed = 1.5

    # 创建飞船
    ship = Ship(setting, screen)

    # 存储子弹
    bullets = Group()

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(setting, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(setting, screen, ship, bullets)


run_game()
