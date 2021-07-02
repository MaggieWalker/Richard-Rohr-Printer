import serial
import adafruit_thermal_printer

def print_extra(num):
    uart = serial.Serial("/dev/serial0", baudrate=19200, timeout=3000)

    ThermalPrinter = adafruit_thermal_printer.get_printer_class(2.19)

    printer = ThermalPrinter(uart)

    printer.feed(num)
    
print_extra(5)