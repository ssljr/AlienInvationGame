import pygame
from pygame.sprite import Sprite
from setting import Setting


class Bullet(Sprite):
    """构建子弹表示子弹的类，继承自 pygame的Sprint类"""

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
        self.keep_shooting = setting.keep_shooting

    def update(self):
        """重写Sprite的update()方法"""
        self.y -= self.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """在屏幕上显示子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)
