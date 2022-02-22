input.onButtonPressed(Button.A, function () {
    basic.showString("lap")
    basic.showNumber(laps)
})
input.onButtonPressed(Button.B, function () {
    basic.showString("step")
    basic.showNumber(steps)
})
input.onGesture(Gesture.Shake, function () {
    steps += 1
})
radio.onReceivedValue(function (name, value) {
    if (name == "serial" && value == control.deviceSerialNumber()) {
        if (flag == 1) {
            flag = 0
            laps += 1
            radio.setGroup(7)
            basic.showIcon(IconNames.SmallSquare)
            flag_just_changed = 1
        }
    } else {
        if (name == "check" && value == control.deviceSerialNumber()) {
            if (flag == 0) {
                flag = 1
                radio.setGroup(11)
                basic.showIcon(IconNames.SmallDiamond)
                flag_just_changed = 1
            }
        }
    }
})
let flag_just_changed = 0
let steps = 0
let flag = 0
let laps = 0
radio.setGroup(7)
radio.setTransmitSerialNumber(true)
laps = 0
flag = 0
steps = 0
flag_just_changed = 0
basic.showIcon(IconNames.SmallHeart)
basic.showIcon(IconNames.Heart)
basic.forever(function () {
    if (flag_just_changed == 1) {
        flag_just_changed = 0
        basic.pause(2000)
    }
    radio.sendNumber(flag)
    basic.pause(10)
})
