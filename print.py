import serial
import adafruit_thermal_printer

def print_snippet(snippet):
    uart = serial.Serial("/dev/serial0", baudrate=19200, timeout=3000)

    ThermalPrinter = adafruit_thermal_printer.get_printer_class(2.19)

    printer = ThermalPrinter(uart)

    printer.feed(2)

    printer.print(snippet)
    printer.feed(5)