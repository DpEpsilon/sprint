from communication import *
from mode import *
from leds import *
from drive import *
from motors import *
from sensors import *

import time

class Roomba(object):
    def __init__(self, port_name, baud_rate, initialize=True, full=False):
        self.communication = Communication(self, port_name, baud_rate)
        self.mode = Mode(self)
        self.leds = Leds(self)
        self.drive = Drive(self)
        self.motors = Motors(self)
        self.sensors = Sensors(self)

        if initialize:
            self.mode.start()   # send start byte
            self.mode.control() # switch to safe mode
            if full:
                self.mode.full()

            time.sleep(0.2)

            # make sure LEDs are reset and motors are stopped initially
            self.leds.update()
            self.drive.update()
            self.motors.update()

    @property
    def communication(self):
        return self._communication
    @communication.setter
    def communication(self, value):
        self._communication = value

    @property
    def mode(self):
        return self._mode
    @mode.setter
    def mode(self, value):
        self._mode = value

    @property
    def leds(self):
        return self._leds
    @leds.setter
    def leds(self, value):
        self._leds = value

    @property
    def drive(self):
        return self._drive
    @drive.setter
    def drive(self, value):
        self._drive = value

    @property
    def motors(self):
        return self._motors
    @motors.setter
    def motors(self, value):
        self._motors = value

    @property
    def sensors(self):
        return self._sensors
    @sensors.setter
    def sensors(self, value):
        self._sensors = value
