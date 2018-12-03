import  pygame
from pygame.sprite import Group

from alien_burst import Alien_Burst
from backgroud_sound import Background_Sound
from background import Background
from button import Button
from game_stats import Game_Stats
from prop import Prop
from scoreboard import Scoreboard
from settings import Settings
from ship import Ship
import game_functions as gf
from shit_sound import Shit_Sound

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    pygame.mixer.init()

    ai_settings = Settings()
    #屏幕设置
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))

    background = Background()

    # 声音设置
    soundwav = Shit_Sound(ai_settings)
    backgound_music = Background_Sound(ai_settings)
    backgound_music.play()
    pygame.display.set_caption("Alien Invasion")
    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Play")

    # 创建存储游戏统计信息的实例，并创建计分牌
    stats = Game_Stats(ai_settings)
    sb = Scoreboard(ai_settings,screen,stats)


    # 创建一艘飞船.存储子弹的编组,一个外星人编组
    ship = Ship(ai_settings,screen)

    bullets = Group()
    aliens = Group()
    props = Group()
    # 显示历史最高纪录
    show_high_score(stats,sb)

    # 创建外星人群
    gf.create_fleet(ai_settings,screen,ship,aliens)

    prop = Prop(ai_settings,screen)
    props.add(prop)
    # 外星人爆炸
    alien_burst = Alien_Burst(screen)
    burst_local = []
    # 开始游戏的主循环

    while True:

        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, stats,sb, play_button, ship,
aliens, bullets,soundwav,backgound_music,background)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets,
                              background,alien_burst,backgound_music)
            gf.update_aliens(ai_settings,stats,sb,screen,ship,aliens,bullets)
            gf.update_prop(ai_settings,screen,props,stats,ship,bullets,soundwav)

        gf.update_screen(ai_settings, screen,stats,sb,ship,aliens, bullets,play_button,
                         props,background,alien_burst,burst_local)



def show_high_score(stats,sb):
    """从文件夹中获取历史最高分并显示"""
    with open("high_score.txt") as f_obj:
        history_high_score = f_obj.read()
        stats.high_score = int(history_high_score.strip())
    gf.check_high_score(stats, sb)
    sb.prep_high_score()
    sb.show_score()


run_game()


