input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    music.playTone(784, music.beat(BeatFraction.Sixteenth))
    if (s > 0) {
        s = s - 1
        bollet_x2 = bollet_x2 - 1
    }
    
    Move(s, 4, bollet_x2, bollet_y2)
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    
    music.playTone(196, music.beat(BeatFraction.Sixteenth))
    bollet_x2 = s
    bollet_y2 = 3
    check = 0
    for (let index = 0; index < 4; index++) {
        basic.clearScreen()
        led.plot(s, 4)
        led.plot(bollet_x2, bollet_y2)
        bollet_y2 = bollet_y2 - 1
        basic.pause(100)
        if (bollet_x2 == rock_x && bollet_y2 == rock_y) {
            check = 1
            break
        }
        
    }
    basic.clearScreen()
    led.plot(s, 4)
    if (check == 1) {
        basic.showIcon(IconNames.Happy)
        music.playMelody("B A G A G F A C5 ", 240)
        basic.pause(1000)
        initial()
    }
    
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    music.playTone(784, music.beat(BeatFraction.Sixteenth))
    if (s < 4) {
        s = s + 1
        bollet_x2 = bollet_x2 + 1
    }
    
    Move(s, 4, bollet_x2, bollet_y2)
})
function initial() {
    
    basic.clearScreen()
    basic.showIcon(IconNames.Yes)
    basic.pause(100)
    music.playMelody("C5 B A G F E D C ", 200)
    basic.clearScreen()
    rock_x = randint(0, 4)
    rock_y = randint(0, 2)
    s = 2
    bollet_x2 = 2
    bollet_y2 = 4
    led.plot(s, 4)
    led.plot(rock_x, rock_y)
}

function Move(player_x: number, player_y: number, bollet_x: number, bollet_y: number) {
    basic.clearScreen()
    led.plot(rock_x, rock_y)
    led.plot(player_x, player_y)
    led.plot(bollet_x, bollet_y)
}

let rock_y = 0
let rock_x = 0
let check = 0
let bollet_y2 = 0
let bollet_x2 = 0
let s = 0
initial()
