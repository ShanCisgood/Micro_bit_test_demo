def on_button_pressed_a():
    global s, bollet_x2
    music.play_tone(784, music.beat(BeatFraction.SIXTEENTH))
    if s > 0:
        s = s - 1
        bollet_x2 = bollet_x2 - 1
    Move(s, 4, bollet_x2, bollet_y2)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global bollet_x2, bollet_y2, check
    music.play_tone(196, music.beat(BeatFraction.SIXTEENTH))
    bollet_x2 = s
    bollet_y2 = 3
    check = 0
    for index in range(4):
        basic.clear_screen()
        led.plot(s, 4)
        led.plot(bollet_x2, bollet_y2)
        bollet_y2 = bollet_y2 - 1
        basic.pause(100)
        if bollet_x2 == rock_x and bollet_y2 == rock_y:
            check = 1
            break
    basic.clear_screen()
    led.plot(s, 4)
    if check == 1:
        basic.show_icon(IconNames.HAPPY)
        music.play_melody("B A G A G F A C5 ", 240)
        basic.pause(1000)
        initial()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global s, bollet_x2
    music.play_tone(784, music.beat(BeatFraction.SIXTEENTH))
    if s < 4:
        s = s + 1
        bollet_x2 = bollet_x2 + 1
    Move(s, 4, bollet_x2, bollet_y2)
input.on_button_pressed(Button.B, on_button_pressed_b)

def initial():
    global rock_x, rock_y, s, bollet_x2, bollet_y2
    basic.clear_screen()
    basic.show_icon(IconNames.YES)
    basic.pause(100)
    music.play_melody("C5 B A G F E D C ", 200)
    basic.clear_screen()
    rock_x = randint(0, 4)
    rock_y = randint(0, 2)
    s = 2
    bollet_x2 = 2
    bollet_y2 = 4
    led.plot(s, 4)
    led.plot(rock_x, rock_y)
def Move(player_x: number, player_y: number, bollet_x: number, bollet_y: number):
    basic.clear_screen()
    led.plot(rock_x, rock_y)
    led.plot(player_x, player_y)
    led.plot(bollet_x, bollet_y)
rock_y = 0
rock_x = 0
check = 0
bollet_y2 = 0
bollet_x2 = 0
s = 0
initial()