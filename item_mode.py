from pico2d import *
import game_framework
import game_world
import play_mode

image = None


def init():
    global image
    image = load_image('item_select.png')


def finish():
    global image
    if image:
        del image
        image = None


def update():
    game_world.update()


def render():
    clear_canvas()
    game_world.render()
    if image:
        image.draw(400, 300)
    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key in (SDLK_0, SDLK_KP_0):
                play_mode.set_ball_type(0)
                game_framework.pop_mode()
            elif event.key in (SDLK_1, SDLK_KP_1):
                play_mode.set_ball_type(1)
                game_framework.pop_mode()
            elif event.key in (SDLK_2, SDLK_KP_2):
                play_mode.set_ball_type(2)
                game_framework.pop_mode()
            elif event.key == SDLK_ESCAPE:
                game_framework.pop_mode()


def pause():
    pass


def resume():
    pass
