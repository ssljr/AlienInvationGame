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
        setting.keep_shooting = True
        # 创建子弹
        fire_bullet(setting, screen, ship, bullets)


# 松开键盘响应操作
def check_keyup_event(event, setting, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_SPACE:
        setting.keep_shooting = False


def fire_bullet(setting, screen, ship, bullets):
    if len(bullets) < setting.bullet_allowed:
        new_bullet = Bullet(setting, screen, ship)
        # 加入到存储子弹到数组
        bullets.add(new_bullet)


def update_bullets(bullets):
    # 刷新显示子弹
    bullets.update()

    # 删除消失的子弹
    for bullet in bullets:
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def update_screen(setting, screen, ship, bullets):
    screen.fill(setting.bg_color)
    # 现实每一颗子弹在屏幕上
    for bullet in bullets:
        bullet.draw_bullet()
    # 显示飞船在屏幕上
    ship.blitme()
    pygame.display.flip()
