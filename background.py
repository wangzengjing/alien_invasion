import pygame


class Background():
    def __init__(self):


        self.background = pygame.image.load("images/0.jpg").convert()




    def update_background(self,level):
        """更新背景图"""
        self.background = pygame.image.load("images/"+str(level-1)+".jpg").convert()