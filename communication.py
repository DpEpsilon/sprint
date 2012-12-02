from common import *

import serial

CMD_BAUD = chr(129)

BAUD_RATES = [300, 600, 1200, 2400, 4800, 9600, 14400, 19200, 28800, 38400, 57600, 115200]

class Communication(Module):
    def __init__(self, parent, port_name, baud_rate):
        self.parent = parent

        if not isinstance(port_name, str):
            raise Exception("Port name must be a string.")
        if not isinstance(baud_rate, int):
            raise Exception("Baud rate must be an integer.")
        if baud_rate not in BAUD_RATES:
            raise Exception("%d is not a valid baud rate; check the SCI Specification for acceptable values." % baud_rate)

        self.port = serial.Serial(port_name, baud_rate)

    def send(self, data):
        if not isinstance(data, str):
            raise Exception("Data must be a string.")
        self.port.write(data)

    def receive(self, length):
        if not isinstance(length, int):
            raise Exception("Receive length must be an integer.")
        return self.port.read(length)

    _port = None
    @property
    def port(self):
        return self._port
    @port.setter
    def port(self, value):
        self._port = value
