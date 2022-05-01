import sys
import pygame

from bullet import Bullet


def check_events(setting, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, setting, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, setting, screen, ship, bullets)


# 按下键盘响应操作
def check_keydown_event(event, setting, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # 创建子弹
        new_bullet = Bullet(setting, screen, ship)
        bullets.add(new_bullet)


# 松开键盘响应操作
def check_keyup_event(event, setting, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(ai_settings, screen, ship, bullets):
    screen.fill(ai_settings.bg_color)

    for bullet in bullets:
        bullet.draw_bullet()
    ship.blitme()
    pygame.display.flip()
