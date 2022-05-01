from typing import Tuple

import pygame


class Ship:
    def __init__(self, setting, screen):
        """初始化飞船，设置其默认位置"""
        self.screen = screen
        self.setting = setting

        # 加载飞船图像，并获取其外接矩形
        self.image = pygame.image.load('images/ship.jpeg')
        # 飞船的矩形位置
        self.rect = self.image.get_rect()
        # 屏幕串口的矩形位置
        self.screen_rect = screen.get_rect()

        # 将每个新飞船，放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False
        self.moving_left = False

        # 定义浮点数，调整速度
        self.center = float(self.rect.centerx)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        # 向右边移动，如果检查到了屏幕最右边，则停止移动
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.setting.ship_center_speed
        # 向左边移动，如果检查到了屏幕最左边，则停止移动
        if self.moving_left and self.rect.left > 0:
            self.center -= self.setting.ship_center_speed
        # 更新最后到位置
        self.rect.centerx = self.center
