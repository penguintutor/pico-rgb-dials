from machine import ADC, Pin
adc = ADC(Pin(28))
print (str(adc.read_u16()))