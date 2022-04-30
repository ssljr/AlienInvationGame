import pygame
import sys
from setting import Setting
from ship import Ship


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()

    set = Setting()
    screen = pygame.display.set_mode((set.screen_width, set.screen_height))
    pygame.display.set_caption('*** 外星风暴 ***')

    # 创建飞船
    ship = Ship(screen)

    # 设置背景颜色
    bg_color = set.bg_color
    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(bg_color)
        ship.blitme()
        # 让最近绘制的屏幕可见
        pygame.display.flip()


run_game()
