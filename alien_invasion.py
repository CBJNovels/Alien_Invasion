import sys
import pygame

from settings import Settings
import game_functions as gf #简称
from ship import Ship

def run_game():
    #初始化游戏并创建一个对象
    pygame.init()
    #设置屏幕宽高、名
    ai_settings=Settings()
    screen=pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #创建一艘飞船
    ship=Ship(screen)

    #开始游戏的主循环
    while True:
        #监视键盘和鼠标事件
        gf.check_events(ship)
        #每次循环都重绘屏幕
        ship.update()
        gf.update_screen(ai_settings,screen,ship)

        #让最近绘制的屏幕可见
        pygame.display.flip()

run_game()