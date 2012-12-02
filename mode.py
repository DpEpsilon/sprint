from common import *

CMD_START = chr(128)
CMD_CONTROL = chr(130)
CMD_SAFE = chr(131)
CMD_FULL = chr(132)
CMD_POWER = chr(133)

class Mode(Module):
    def __init__(self, parent):
        self.parent = parent

    def start(self):
        self.parent.communication.send(CMD_START)

    def control(self):
        self.parent.communication.send(CMD_CONTROL)

    def safe(self):
        self.parent.communication.send(CMD_SAFE)

    def full(self):
        self.parent.communication.send(CMD_FULL)

    def power(self):
        self.parent.communication.send(CMD_POWER)
