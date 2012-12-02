from common import *

CMD_LEDS = chr(139)

LED_STATUS_MIN = 0b00
LED_STATUS_MAX = 0b11
LED_STATUS_OFF = 0b00
LED_STATUS_RED = 0b01
LED_STATUS_GREEN = 0b10
LED_STATUS_AMBER = 0b11

LED_POWER_COLOR_MIN = 0
LED_POWER_COLOR_MAX = 255
LED_POWER_COLOR_GREEN = 0
LED_POWER_COLOR_AMBER = 128
LED_POWER_COLOR_RED = 255

LED_POWER_INTENSITY_MIN = 0
LED_POWER_INTENSITY_MAX = 255
LED_POWER_INTENSITY_OFF = 0
LED_POWER_INTENSITY_MID = 128
LED_POWER_INTENSITY_FULL = 255

class Leds(Module):
    def __init__(self, parent):
        self.parent = parent

    def update(self):
        first = (self.status << 4) | (self.spot << 3) | (self.clean << 2) | (self.max << 1) | self.dirt_detect
        data = CMD_LEDS + chr(first) + chr(self.power_color) + chr(self.power_intensity)
        self.parent.communication.send(data)

    _status = LED_STATUS_OFF
    @property
    def status(self):
        return self._status
    @status.setter
    def status(self, value):
        if not isinstance(value, int):
            raise Exception("Status LED value must be an integer.")
        if value < LED_STATUS_MIN or value > LED_STATUS_MAX:
            raise Exception("Invalid value for status LED; it must lie between %d and %d." % (LED_STATUS_MIN, LED_STATUS_MAX))
        self._status = value
        self.update()

    _spot = False
    @property
    def spot(self):
        return self._spot
    @spot.setter
    def spot(self, value):
        if not isinstance(value, bool):
            raise Exception("LED value must be a bool.")
        self._spot = value
        self.update()

    _clean = False
    @property
    def clean(self):
        return self._clean
    @clean.setter
    def clean(self, value):
        if not isinstance(value, bool):
            raise Exception("LED value must be a bool.")
        self._clean = value
        self.update()

    _max = False
    @property
    def max(self):
        return self._max
    @max.setter
    def max(self, value):
        if not isinstance(value, bool):
            raise Exception("LED value must be a bool.")
        self._max = value
        self.update()

    _dirt_detect = False
    @property
    def dirt_detect(self):
        return self._dirt_detect
    @dirt_detect.setter
    def dirt_detect(self, value):
        if not isinstance(value, bool):
            raise Exception("LED value must be a bool.")
        self._dirt_detect = value
        self.update()

    _power_color = LED_POWER_COLOR_RED
    @property
    def power_color(self):
        return self._power_color
    @power_color.setter
    def power_color(self, value):
        if not isinstance(value, int):
            raise Exception("Power LED color value must be an integer.")
        if value < LED_POWER_COLOR_MIN or value > LED_POWER_COLOR_MAX:
            raise Exception("Invalid value for power LED color value; it must lie between %d and %d." % (LED_POWER_COLOR_MIN, LED_POWER_COLOR_MAX))
        self._power_color = value
        self.update()

    _power_intensity = LED_POWER_INTENSITY_MID
    @property
    def power_intensity(self):
        return self._power_intensity
    @power_intensity.setter
    def power_intensity(self, value):
        if not isinstance(value, int):
            raise Exception("Power LED intensity value must be an integer.")
        if value < LED_POWER_INTENSITY_MIN or value > LED_POWER_INTENSITY_MAX:
            raise Exception("INvalid value for power LED intensity value; it must lie between %d and %d." % (LED_POWER_INTENSITY_MIN, LED_POWER_INTENSITY_MAX))
        self._power_intensity = value
        self.update()
