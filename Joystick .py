# Write your code here :-)
from microbit import *
import music

note_c = ["C:4"]
note_d = ["D:4"]
note_e = ["E:4"]
note_f = ["F:4"]
note_g = ["G:4"]
note_a = ["A:4"]

while True:
        #X-Axis
        value_a = pin1.read_analog()
        if value_a < 300:
            music.play(note_c)
            #display.scroll("1")
        elif value_a > 600:
            music.play(note_e)
            #display.scroll("2")

        #Y-Axis
        value_b = pin2.read_analog()

        if value_b < 300:
            music.play(note_d)
            #display.scroll("4")
        elif value_b > 600:
            music.play(note_f)
            #display.scroll("3")

        if (button_a.is_pressed()):
            music.play(note_g)

        if (button_b.is_pressed()):
            music.play(note_a)

        #if pin8.read_digital() == 0:
            #music.play(note_a)
            #display.show(1)

        else:
            display.show(Image.HAPPY)
            sleep(100)
            display.clear()


