import random

import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """表示单个外星人的类"""

    def __init__(self,ai_settings,screen,num):
        """初始化外星人并设置其起始位置"""
        super(Alien,self).__init__()

        self.screen = screen
        self.ai_settings = ai_settings

        # 加载外星人图像，并设置其rect属性
        self.image = pygame.image.load("images/alien"+str(num)+".png")
        self.rect = self.image.get_rect()

        # 每个外星人最初都在屏幕左上角附近
        self.rect.x = random.randint(10,800)
        self.rect.y = random.randint(-100,-50)

        # 存储外星人的精确位置
        self.x =float(self.rect.x)
        self.y = float(self.rect.y)

        # 存储外星人每次移动的距离
        self.up_distance = 0
        self.drop_distance = 0
        self.left_distance = self.rect.x
        self.right_distance = self.rect.x

        self.right_direction = 1
        self.left_direction = 1

    def biltme(self):
        """在指定位置绘制外星人"""
        self.screen.blit(self.image,self.rect)




    def check_edges(self):
        """如果外星人位于屏幕边缘，就返回True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right :
            return 'right'
        elif self.rect.left <=0 :
            return 'left'

    def right_move(self):
        """向左或右移动外星人"""
        self.x += self.ai_settings.alien_speed_factor * self.right_direction
        self.rect.x = self.x

    def left_move(self):
        """向左或右移动外星人"""
        self.x -= self.ai_settings.alien_speed_factor * self.left_direction
        self.rect.x = self.x

    def drop_move(self):
        self.y +=self.ai_settings.alien_speed_factor
        self.rect.y = self.y

    def up_move(self):
        self.y -=self.ai_settings.alien_speed_factor
        self.rect.y = self.y
