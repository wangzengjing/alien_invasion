import pygame
from datetime import datetime


class Settings():
    """存储<外星人入侵>的所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""

        # 屏幕设置
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230,230,230)
        self.Fullscreen = False



        # 飞船的设置
        self.ship_limit = 3

        # 子弹设置
        self.bullet_width = 10
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 10
        self.bullet_unbeatable = False

        self.bullet_laser = False

        # 外星人设置
        self.fleet_drop_speed = 5
        self.drop = 0
        self.drop_distance = []

        # fleet_direction为1表示向右移，为-1表示向左移
        self.fleet_direction = []


        # 道具移动速度
        self.prop_move_speed = 0.5

        # 道具维持时间
        self.prop_start_time = datetime.now()

        self.prop_time = 15

        # 爆炸效果维持时间
        self.burst_time = datetime.now()

        # 音乐内容控制
        # 1为普通射击声音，2为激光射击声音
        self.shit_sound = 1


        # 以什么样的速度加快游戏节奏
        self.speedup_scale = 1.1

        # 外星人点数的提高速度
        self.score_scale = 1.5

        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed_factor = 1
        self.bullet_speed_factor = 1
        self.alien_speed_factor = 0.3




        # 记分
        self.alien_points = 50

    def increase_speed(self):
        """提高速度设置"""

        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)

