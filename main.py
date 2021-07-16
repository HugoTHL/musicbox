def on_button_pressed_a():
    global volume
    volume += 20
    music.set_volume(volume)
    basic.show_string("" + str((volume)))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.show_leds("""
        . . . . .
                . # . # .
                . . . . .
                # . . . #
                . # # # .
    """)
    music.start_melody(music.built_in_melody(Melodies.BIRTHDAY), MelodyOptions.ONCE)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global volume
    volume = volume - 20
    music.set_volume(volume)
    basic.show_string("" + str((volume)))
input.on_button_pressed(Button.B, on_button_pressed_b)

volume = 0
volume = 10
basic.show_leds("""
    . . . . .
        . # . # .
        . . . . .
        # . . . #
        . # # # .
""")