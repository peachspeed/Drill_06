from pico2d import *
import random


TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)


tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')


running = True
frame = 0
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
hand_x, hand_y = random.randint(0, TUK_WIDTH), random.randint(0, TUK_HEIGHT)  # 손의 초기 랜덤 위치
dir = 1
speed = 5


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def update_character_position():
    global x, y, hand_x, hand_y, dir


    if x < hand_x:
        x += speed
        dir = 1
    elif x > hand_x:
        x -= speed
        dir = -1

    if y < hand_y:
        y += speed
    elif y > hand_y:
        y -= speed


    if abs(x - hand_x) < 10 and abs(y - hand_y) < 10:

        hand_x, hand_y = random.randint(0, TUK_WIDTH), random.randint(0, TUK_HEIGHT)


hide_cursor()


while running:
    clear_canvas()


    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)


    hand.draw(hand_x, hand_y)


    if dir == 1:
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
    else:
        character.clip_draw(frame * 100, 0, 100, 100, x, y)


    update_canvas()


    update_character_position()


    handle_events()


    frame = (frame + 1) % 8
    delay(0.05)

close_canvas()