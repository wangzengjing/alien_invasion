import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """一个对飞船发射的子弹进行管理的类"""
    def __init__(self,ai_settings,screen,ship):
        """在飞船所处的位置创建一个子弹对象"""
        super(Bullet,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # 加载外星人图像，并设置其rect属性
        if self.ai_settings.bullet_laser:
            self.image = pygame.image.load("images/laser.png")
        else:
            self.image = pygame.image.load("images/zidan.png")
        self.rect = self.image.get_rect()

        # 在(0,0)处创建一个表示子弹的矩形，再设置正确的位置
       # self.rect = pygame.Rect(0,0,ai_settings.bullet_width,
      #     ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.bottom = ship.rect.top

        # 存储用小数表示的子弹位置
        self.y = float(ship.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor


    def update(self):
        """向上移动子弹"""
        # 更新表示子弹位置的小数值
        self.y -= self.speed_factor

        # 更新表示子弹的rect的位置
        self.rect.bottom = self.y + 20



    def biltme(self):
            """在指定位置绘制子弹"""
            self.screen.blit(self.image,self.rect)

