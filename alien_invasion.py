import pygame
import game_functions as gf
from setting import Setting
from ship import Ship


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()

    setting = Setting()
    screen = pygame.display.set_mode((setting.screen_width, setting.screen_height))
    pygame.display.set_caption('*** 外星风暴 ***')

    # 创建飞船
    ship = Ship(screen)

    # 设置背景颜色
    bg_color = setting.bg_color
    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events()

        screen.fill(bg_color)
        ship.blitme()
        # 让最近绘制的屏幕可见
        pygame.display.flip()


run_game()
