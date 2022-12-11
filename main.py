def on_button_pressed_a():
    global led2
    led2 += 1
    if led2 == 3:
        led2 = 0
input.on_button_pressed(Button.A, on_button_pressed_a)

def changeLEDS():
    if led2 == 0:
        pins.analog_write_pin(AnalogPin.P1, water)
        pins.analog_write_pin(AnalogPin.P2, 0)
        pins.analog_write_pin(AnalogPin.P8, 0)
    elif led2 == 1:
        pins.analog_write_pin(AnalogPin.P1, 0)
        pins.analog_write_pin(AnalogPin.P8, 0)
        pins.analog_write_pin(AnalogPin.P2, water)
    else:
        pins.analog_write_pin(AnalogPin.P1, 0)
        pins.analog_write_pin(AnalogPin.P2, 0)
        pins.analog_write_pin(AnalogPin.P8, water)
water = 0
led2 = 0
led2 = 0
pins.set_pull(DigitalPin.P11, PinPullMode.PULL_UP)

def on_forever():
    global led2, water
    if pins.digital_read_pin(DigitalPin.P11) == 0:
        led2 += 1
        if led2 == 3:
            led2 = 0
    water = pins.analog_read_pin(AnalogPin.P0)
    led.plot_bar_graph(pins.analog_read_pin(AnalogPin.P0), 1023)
    changeLEDS()
basic.forever(on_forever)
