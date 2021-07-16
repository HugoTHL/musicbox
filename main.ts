input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    volume += 20
    music.setVolume(volume)
    basic.showString("" + ("" + volume))
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    basic.showLeds(`
        . . . . .
                . # . # .
                . . . . .
                # . . . #
                . # # # .
    `)
    music.startMelody(music.builtInMelody(Melodies.Birthday), MelodyOptions.Once)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    volume = volume - 20
    music.setVolume(volume)
    basic.showString("" + ("" + volume))
})
let volume = 0
volume = 10
basic.showLeds(`
    . . . . .
        . # . # .
        . . . . .
        # . . . #
        . # # # .
`)
