from common import *

import struct

CMD_DRIVE = chr(137)

VELOCITY_MIN = -500
VELOCITY_MAX = 500
VELOCITY_STOP = 0

RADIUS_MIN = -2000
RADIUS_MAX = 2000
RADIUS_STRAIGHT = 0
RADIUS_LEFT = 1
RADIUS_RIGHT = -1

class Drive(Module):
    def __init__(self, parent):
        self.parent = parent

    def update(self):
        velocity_l, velocity_h = struct.pack('h', self.velocity)
        radius_l, radius_h = struct.pack('h', self.radius)

        data = CMD_DRIVE + velocity_h + velocity_l + radius_h + radius_l
        self.parent.communication.send(data)

    def forward(self, velocity):
        self.radius = RADIUS_STRAIGHT
        self.velocity = velocity

    def reverse(self, velocity):
        self.radius = RADIUS_STRAIGHT
        self.velocity = -velocity

    def spin_left(self, velocity):
        self.radius = RADIUS_LEFT
        self.velocity = velocity

    def spin_right(self, velocity):
        self.radius = RADIUS_RIGHT
        self.velocity = velocity

    def stop(self):
        self.velocity = 0

    _velocity = 0
    @property
    def velocity(self):
        return self._velocity
    @velocity.setter
    def velocity(self, value):
        if not isinstance(value, int):
            raise Exception("Velocity must be an integer.")
        if value < VELOCITY_MIN or value > VELOCITY_MAX:
            raise Exception("Invalid value for velocity; it must lie between %d and %d." % (VELOCITY_MIN, VELOCITY_MAX))
        self._velocity = value
        self.update()

    _radius = RADIUS_STRAIGHT
    @property
    def radius(self):
        return self._radius
    @radius.setter
    def radius(self, value):
        if not isinstance(value, int):
            raise Exception("Radius must be an integer.")
        if value < RADIUS_MIN or value > RADIUS_MAX:
            raise Exception("Invalid value for radius; it must lie between %d and %d." % (RADIUS_MIN, RADIUS_MAX))
        self._radius = value
        self.update()
