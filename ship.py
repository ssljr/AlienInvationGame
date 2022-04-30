import pygame


class Ship:
    def __init__(self, screen):
        """初始化飞船，设置其默认位置"""
        self.screen = screen

        # 加载飞船图像，并获取其外接矩形
        self.image = pygame.image.load('images/ship.jpeg')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每个新飞船，放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)
