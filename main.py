def on_button_pressed_a():
    basic.show_string("Laps")
    basic.show_number(laps)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_string("Steps")
    basic.show_number(steps)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    global steps
    steps += 1
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_received_value(name, value):
    global flag, laps
    if name == "serial" and value == control.device_serial_number():
        if flag == 1:
            flag = 0
            laps += 1
            radio.set_group(7)
            music.play_tone(294, music.beat(BeatFraction.HALF))
            music.play_tone(262, music.beat(BeatFraction.HALF))
            basic.pause(5000)
    if name == "check" and value == control.device_serial_number():
        if flag == 0:
            flag = 1
            radio.set_group(11)
            music.play_tone(262, music.beat(BeatFraction.HALF))
            basic.pause(5000)
radio.on_received_value(on_received_value)

steps = 0
flag = 0
laps = 0
radio.set_group(7)
radio.set_transmit_serial_number(True)
laps = 0
flag = 0
steps = 0
basic.show_icon(IconNames.SMALL_HEART)
basic.show_icon(IconNames.HEART)

def on_forever():
    radio.send_number(flag)
    basic.pause(10)
basic.forever(on_forever)
