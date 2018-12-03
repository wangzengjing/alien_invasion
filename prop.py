import pygame
from pygame.sprite import Sprite


class Prop(Sprite):
    def __init__(self,ai_settings,screen):
        super(Prop,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载道具图像
        self.image = pygame.image.load("images/prop.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()


        # 将道具放在屏幕左上角测试

        self.rect.centerx = self.rect.width
        self.rect.bottom = self.rect.height

        self.center = float(self.rect.centerx)
        self.bottomy = float(self.rect.bottom)

        # 道具的左右上下移动,prop_x_direction True 为向右移动,False相反
        #   prop_y_direction True 为向上移动,False相反,
        self.prop_x_direction = True
        self.prop_y_direction = True

    def update(self):
        """根据标识移动位置"""
        if self.prop_x_direction :
            self.center += self.ai_settings.prop_move_speed
        else:
            self.center -= self.ai_settings.prop_move_speed

        if self.prop_y_direction :
            self.bottomy -= self.ai_settings.prop_move_speed
        else:
            self.bottomy += self.ai_settings.prop_move_speed

        # 根据self.center更新rect对象
        self.rect.x = self.center
        self.rect.y = self.bottomy

    def blitme(self):
        """绘制道具"""
        self.screen.blit(self.image,self.rect)
