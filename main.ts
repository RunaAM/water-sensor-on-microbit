input.onButtonPressed(Button.A, function () {
    led2 += 1
    if (led2 == 3) {
        led2 = 0
    }
})
function changeLEDS () {
    if (led2 == 0) {
        pins.analogWritePin(AnalogPin.P1, water)
        pins.analogWritePin(AnalogPin.P2, 0)
        pins.analogWritePin(AnalogPin.P8, 0)
    } else if (led2 == 1) {
        pins.analogWritePin(AnalogPin.P1, 0)
        pins.analogWritePin(AnalogPin.P2, water)
        pins.analogWritePin(AnalogPin.P8, 0)
    } else {
        pins.analogWritePin(AnalogPin.P1, 0)
        pins.analogWritePin(AnalogPin.P2, 0)
        pins.analogWritePin(AnalogPin.P8, water)
    }
}
let water = 0
let led2 = 0
led2 = 0
pins.setPull(DigitalPin.P11, PinPullMode.PullUp)
basic.forever(function () {
    if (pins.digitalReadPin(DigitalPin.P11) == 0) {
        led2 += 1
        if (led2 == 3) {
            led2 = 0
        }
    }
    water = pins.analogReadPin(AnalogPin.P0)
    led.plotBarGraph(
    pins.analogReadPin(AnalogPin.P0),
    1023
    )
    changeLEDS()
})
