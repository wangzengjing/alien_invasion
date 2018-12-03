import pygame


class Background_Sound:
    def __init__(self,ai_settings):
        """控制游戏各种声音"""

        self.ai_settings= ai_settings
        # 加载射击声音

        self.soundwav = pygame.mixer.music.load("sound/start_game.mp3")

        self.alien_burst_sound =  pygame.mixer.Sound("sound/burst.wav")


    def update_music(self):
        """更新射击声音"""

    def play(self,roll=-1):
        """开始播放射击音乐"""
        pygame.mixer.music.play(roll)

    def stop(self):
        """暂停播放音乐"""
        pygame.mixer.music.stop()

    def fadeout(self,time):
        pygame.mixer.music.fadeout(time)

    def alien_burst_play(self):
        self.alien_burst_sound.play()

    def alien_burst_stop(self):
        self.alien_burst_sound.stop()

    def alien_burst_fadeout(self,time):
        self.alien_burst_sound.fadeout(time)