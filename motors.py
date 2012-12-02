from common import *

CMD_MOTORS = chr(138)

class Motors(Module):
    def __init__(self, parent):
        self.parent = parent

    def update(self):
        first = (self.main_brush << 2) | (self.vacuum << 1) | self.side_brush
        data = CMD_MOTORS + chr(first)
        self.parent.communication.send(data)

    _main_brush = False
    @property
    def main_brush(self):
        return self._main_brush
    @main_brush.setter
    def main_brush(self, value):
        if not isinstance(value, bool):
            raise Exception("Main brush value must be a bool.")
        self._main_brush = value
        self.update()

    _vacuum = False
    @property
    def vacuum(self):
        return self._vacuum
    @vacuum.setter
    def vacuum(self, value):
        if not isinstance(value, bool):
            raise Exception("Vacuum value must be a bool.")
        self._vacuum = value
        self.update()

    _side_brush = False
    @property
    def side_brush(self):
        return self._side_brush
    @side_brush.setter
    def side_brush(self, value):
        if not isinstance(value, bool):
            raise Exception("Side brush value must be a bool.")
        self._side_brush = value
        self.update()
