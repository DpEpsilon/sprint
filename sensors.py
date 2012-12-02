from common import *

CMD_SENSORS = chr(142)

SENSOR_ONE = (1 << 0)
SENSOR_TWO = (1 << 1)
SENSOR_THREE = (1 << 2)

SENSOR_BUMP = SENSOR_ONE
SENSOR_WHEELDROP = SENSOR_ONE
SENSOR_WALL = SENSOR_ONE
SENSOR_CLIFF = SENSOR_ONE
SENSOR_VIRTUAL_WALL = SENSOR_ONE
SENSOR_OVERCURRENT = SENSOR_ONE
SENSOR_DIRT_DETECTOR = SENSOR_ONE
SENSOR_REMOTE_CONTROL = SENSOR_TWO
SENSOR_BUTTONS = SENSOR_TWO
SENSOR_DISTANCE = SENSOR_TWO
SENSOR_ANGLE = SENSOR_TWO
SENSOR_CHARGING_STATE = SENSOR_THREE
SENSOR_VOLTAGE = SENSOR_THREE
SENSOR_CURRENT = SENSOR_THREE
SENSOR_TEMPERATURE = SENSOR_THREE
SENSOR_CHARGE = SENSOR_THREE
SENSOR_CAPACITY = SENSOR_THREE

class SensorData(object):
    def add_data(self, data, packet_code):
        if packet_code == 0:
            # split it into packets 1, 2 and 3 and call add_data for each
            self.add_data(data[:10], 1)
            self.add_data(data[10:16], 2)
            self.add_data(data[16:26], 3)
        elif packet_code == 1:
            self.bump_right = (data[0] & (1 << 0))
            self.bump_left = (data[0] & (1 << 1))
            self.wheeldrop_right = (data[0] & (1 << 2))
            self.wheeldrop_left = (data[0] & (1 << 3))
            self.wheeldrop_caster = (data[0] & (1 << 4))
            self.wall = data[1]
            self.cliff_left = data[2]
            self.cliff_front_left = data[3]
            self.cliff_front_right = data[4]
            self.cliff_right = data[5]
            self.virtual_wall = data[6]
            self.overcurrent_side_brush = (data[7] & (1 << 0))
            self.overcurrent_vacuum = (data[7] & (1 << 1))
            self.overcurrent_main_brush = (data[7] & (1 << 2))
            self.overcurrent_drive_right = (data[7] & (1 << 3))
            self.overcurrent_drive_left = (data[7] & (1 << 4))
            self.dirt_detector_left = data[8]
            self.dirt_detector_right = data[9]
        elif packet_code == 2:
            pass
        elif packet_code == 3:
            pass

    _bump_right = None
    @property
    def bump_right(self):
        return self._bump_right
    @bump_right.setter
    def bump_right(self, value):
        self._bump_right = bool(value)

    _bump_left = None
    @property
    def bump_left(self):
        return self._bump_left
    @bump_left.setter
    def bump_left(self, value):
        self._bump_left = bool(value)

    _wheeldrop_left = None
    @property
    def wheeldrop_left(self):
        return self._wheeldrop_left
    @wheeldrop_left.setter
    def wheeldrop_left(self, value):
        self._wheeldrop_left = bool(value)

    _wheeldrop_right = None
    @property
    def wheeldrop_right(self):
        return self._wheeldrop_right
    @wheeldrop_right.setter
    def wheeldrop_right(self, value):
        self._wheeldrop_right = bool(value)

    _wheeldrop_caster = None
    @property
    def wheeldrop_caster(self):
        return self._wheeldrop_caster
    @wheeldrop_caster.setter
    def wheeldrop_caster(self, value):
        self._wheeldrop_caster = bool(value)

    _wall = None
    @property
    def wall(self):
        return self._wall
    @wall.setter
    def wall(self, value):
        self._wall = bool(value)

    _cliff_left = None
    @property
    def cliff_left(self):
        return self._cliff_left
    @cliff_left.setter
    def cliff_left(self, value):
        self._cliff_left = bool(value)

    _cliff_front_left = None
    @property
    def cliff_front_left(self):
        return self._cliff_front_left
    @cliff_front_left.setter
    def cliff_front_left(self, value):
        self._cliff_front_left = bool(value)

    _cliff_front_right = None
    @property
    def cliff_front_right(self):
        return self._cliff_front_right
    @cliff_front_right.setter
    def cliff_front_right(self, value):
        self._cliff_front_right = bool(value)

    _cliff_right = None
    @property
    def cliff_right(self):
        return self._cliff_right
    @cliff_right.setter
    def cliff_right(self, value):
        self._cliff_right = bool(value)

    _virtual_wall = None
    @property
    def virtual_wall(self):
        return self._virtual_wall
    @virtual_wall.setter
    def virtual_wall(self, value):
        self._virtual_wall = bool(value)

    _overcurrent_side_brush = None
    @property
    def overcurrent_side_brush(self):
        return self._overcurrent_side_brush
    @overcurrent_side_brush.setter
    def overcurrent_side_brush(self, value):
        self._overcurrent_side_brush = bool(value)

    _overcurrent_vacuum = None
    @property
    def overcurrent_vacuum(self):
        return self._overcurrent_vacuum
    @overcurrent_vacuum.setter
    def overcurrent_vacuum(self, value):
        self._overcurrent_vacuum = bool(value)

    _overcurrent_main_brush = None
    @property
    def overcurrent_main_brush(self):
        return self._overcurrent_main_brush
    @overcurrent_main_brush.setter
    def overcurrent_main_brush(self, value):
        self._overcurrent_main_brush = bool(value)

    _overcurrent_drive_right = None
    @property
    def overcurrent_drive_right(self):
        return self._overcurrent_drive_right
    @overcurrent_drive_right.setter
    def overcurrent_drive_right(self, value):
        self._overcurrent_drive_right = bool(value)

    _overcurrent_drive_left = None
    @property
    def overcurrent_drive_left(self):
        return self._overcurrent_drive_left
    @overcurrent_drive_left.setter
    def overcurrent_drive_left(self, value):
        self._overcurrent_drive_left = bool(value)

    _dirt_detector_left = None
    @property
    def dirt_detector_left(self):
        return self._dirt_detector_left
    @dirt_detector_left.setter
    def dirt_detector_left(self, value):
        self._dirt_detector_left = bool(value)

    _dirt_detector_right = None
    @property
    def dirt_detector_right(self):
        return self._dirt_detector_right
    @dirt_detector_right.setter
    def dirt_detector_right(self, value):
        self._dirt_detector_right = bool(value)

class Sensors(Module):
    def __init__(self, parent):
        self.parent = parent

    def get_packet(self, packet_code):
        if not isinstance(packet_code, int):
            raise Exception("Packet code must be an integer.")
        if packet_code < 0 or packet_code > 3:
            raise Exception("Invalid packet code; it must lie between 0 and 3.")

        data = CMD_SENSORS + chr(packet_code)
        self.parent.communication.send(data)

        if packet_code == 0:
            return map(ord, self.parent.communication.receive(26))
        elif packet_code == 1:
            return map(ord, self.parent.communication.receive(10))
        elif packet_code == 2:
            return map(ord, self.parent.communication.receive(6))
        elif packet_code == 3:
            return map(ord, self.parent.communication.receive(10))

    def read(self, mask):
        data_object = SensorData()

        if mask & (SENSOR_ONE | SENSOR_TWO | SENSOR_THREE):
            # packet 0
            data_object.add_data(self.get_packet(0), 0)
        else:
            if mask & SENSOR_ONE:
                # packet 1
                data_object.add_data(self.get_packet(1), 1)
            if mask & SENSOR_TWO:
                # packet 2
                data_object.add_data(self.get_packet(2), 2)
            if mask & SENSOR_THREE:
                # packet 3
                data_object.add_data(self.get_packet(3), 3)

        return data_object
