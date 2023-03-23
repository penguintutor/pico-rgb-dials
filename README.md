# pico-rgb-dials
RGB potentiometers to NeoPixels for a Raspberry Pi Pico

Control addressable RGB LEDs (NeoPixels) using 3 potentiometers representing the 3 RGB colours.



# neopixel_rgb.py

The main program. Connect three 10K Pots as voltage dividers to ADC0, ADC1 and ADC2.

Connect two NeoPixels to GPIO 6.

Run the program and turn the dials to change the RGB values.


# read_adc_singlepin.py

Read a single ADC pin and provide it's value between 0 and 65535


# read_adc.py

Read the 3 ADC pins on the Raspberry Pi Pico and output their values as voltages between 0 and 3.3V.