from machine import ADC, Pin
import time

adc_1 = ADC(Pin(26))
adc_2 = ADC(Pin(27))
adc_3 = ADC(Pin(28))

while True:
    red_value = adc_1.read_u16() / 19859
    green_value = adc_2.read_u16() / 19859
    blue_value = adc_3.read_u16() / 19859
    print("ADC0 {} ADC1 {} ADC2 {}".format(red_value, green_value, blue_value))
    time.sleep(1)