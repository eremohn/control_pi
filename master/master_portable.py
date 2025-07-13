import time
import board
import RPi.GPIO as GPIO
from adafruit_ina219 import ADCResolution, BusVoltageRange, INA219
GPIO.setmode(GPIO.BCM)  #segun gpio
GPIO.setup(23, GPIO.OUT) #led testigo
i2c_bus = board.I2C()
ina219 = INA219(i2c_bus)
# optional : change configuration to use 32 samples averaging for both bus voltage and shunt voltage
ina219.bus_adc_resolution = ADCResolution.ADCRES_12BIT_32S
ina219.shunt_adc_resolution = ADCResolution.ADCRES_12BIT_32S
# optional : change voltage range to 16V
ina219.bus_voltage_range = BusVoltageRange.RANGE_32V

# measure and display loop
while True:
    bus_voltage = ina219.bus_voltage  # voltage on V- (load side)
    shunt_voltage = ina219.shunt_voltage  # voltage between V+ and V- across the shunt
    current = ina219.current  # current in mA
    power = ina219.power  # power in watts
    testigo = 23
    # INA219 measure bus voltage on the load side. So PSU voltage = bus_voltage + shunt_voltage
    print("Voltage (VIN+) : {:6.3f}   V".format(bus_voltage + shunt_voltage))
    print("Voltage (VIN-) : {:6.3f}   V".format(bus_voltage))
    print("Shunt Voltage  : {:8.5f} V".format(shunt_voltage))
    print("Shunt Current  : {:7.4f}  A".format(current / 1000))
    print("Power Calc.    : {:8.5f} W".format(bus_voltage * (current / 1000)))
    print("Power Register : {:6.3f}   W".format(power))
    print("")

    key=True

    if bus_voltage <= 17:
        while(key):
           GPIO.output(testigo,False)
           time.sleep(1)
           GPIO.output(testigo,True)
           time.sleep(1)
           key=False
        #GPIO.output(testigo,False)
    elif bus_voltage > 17:
        GPIO.output(testigo,True)
    elif ina219.overflow:
        print("Internal Math Overflow Detected!")
        print("")

    time.sleep(0.5)
