import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """对子弹发射管理"""

    def __init__(self, setting, screen, ship):
        """在飞船位置处创建子弹"""
        super(Bullet, self).__init__()
        self.screen = screen

        # 在(0,0)处创建子弹和设置位置
        self.rect = pygame.Rect(0, 0, setting.bullet_width, setting.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # 用浮点数存储子弹的位置
        self.y = float(self.rect.y)

        self.color = setting.bullet_color
        self.bullet_speed = setting.bullet_speed

    def update(self):
        self.y -= self.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
