from pico2d import *
import game_framework
import game_world
import title_mode
import pause_mode
import item_mode
from boy import Boy
from grass import Grass

boy = None


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.change_mode(title_mode)
            elif event.key == SDLK_p:
                game_framework.push_mode(pause_mode)
            elif event.key == SDLK_i:
                game_framework.push_mode(item_mode)
            else:
                boy.handle_event(event)
        else:
            boy.handle_event(event)


def init():
    global boy

    boy = Boy()
    game_world.add_oject(boy)

    grass = Grass()
    game_world.add_oject(grass, 0)


def finish():
    game_world.clear()


def update():
    game_world.update()


def render():
    clear_canvas()
    game_world.render()
    update_canvas()


def pause():
    pass


def resume():
    if boy and boy.state == 'IDLE':
        boy.idle_started_at = get_time()


def set_ball_type(ball_type):
    if boy:
        boy.ball_type = ball_type
