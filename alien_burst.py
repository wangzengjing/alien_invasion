import pygame


class Alien_Burst():
    """表示外星人爆炸的类"""

    def __init__(self,screen):
        """初始化爆炸效果并设置其起始位置"""

        self.screen = screen


        # 加载外星人图像，并设置其rect属性
        self.image = pygame.image.load("images/burst.png")
        self.rect = self.image.get_rect()

        # 每个外星人最初都在屏幕左上角附近
        self.rect.x = -50
        self.rect.y = -50

    def biltme(self):
        """在指定位置绘制爆炸效果"""
        self.screen.blit(self.image,self.rect)

    def update(self,x,y):
        """更新外星人爆炸效果位置"""

        self.rect.x = x
        self.rect.y = y
    def reset_burst(self):
        self.rect.x = -50
        self.rect.y = -50
