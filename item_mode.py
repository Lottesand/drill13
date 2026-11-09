from pico2d import *
import game_framework
import game_world

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
    pass


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


def pause():
    pass


def resume():
    pass
