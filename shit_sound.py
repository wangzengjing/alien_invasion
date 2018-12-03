import pygame


class Shit_Sound:
    def __init__(self,ai_settings):
        """控制游戏各种声音"""

        self.ai_settings= ai_settings
        # 加载射击声音

        self.soundwav = pygame.mixer.Sound("sound/shit.wav")



    def update_music(self):
        """更新射击声音"""
        if self.ai_settings.shit_sound == 1:
            self.soundwav = pygame.mixer.Sound("sound/shit.wav")
        elif self.ai_settings.shit_sound == 2:
            self.soundwav = pygame.mixer.Sound("sound/laser.wav")

    def play(self):
        """开始播放射击音乐"""
        self.soundwav.play()

    def stop(self):
        """暂停播放音乐"""
        self.soundwav.stop()

    def fadeout(self,time):
        self.soundwav.fadeout(time)