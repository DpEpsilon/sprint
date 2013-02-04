from common import *

import struct

CMD_SENSORS = chr(142)
CMD_QUERY_LIST = chr(149)
CMD_WAIT_DISTANCE = chr(156)
CMD_WAIT_ANGLE = chr(157)

class Sensors(Module):
    def __init__(self, parent):
        self.parent = parent

    def get_packet(self, packet_code, return_bytes=False):
        if not isinstance(packet_code, int):
            raise Exception("Packet code must be an integer.")
        if packet_code < 0 or packet_code > 42:
            raise Exception("Invalid packet code; it must lie between 0 and 42.")

        data = CMD_SENSORS + chr(packet_code)
        self.parent.communication.send(data)

        if packet_code == 0:
            length = 26
        elif packet_code == 1 or packet_code == 3:
            length = 10
        elif packet_code == 2:
            length = 6
        elif (packet_code >= 7 and packet_code <= 18) or packet_code == 21 or packet_code == 24 or packet_code == 32 or (packet_code >= 34 and packet_code <= 38):
            length = 1
        else:
            length = 2

        data = self.parent.communication.receive(length)
        if return_bytes:
            return data
        else:
            return map(ord, data)

    def bumper_left(self):
        return bool(self.get_packet(7)[0] & 0b00000010)

    def bumper_right(self):
        return bool(self.get_packet(7)[0] & 0b00000001)

    def wheeldrop_left(self):
        return bool(self.get_packet(7)[0] & 0b00001000)

    def wheeldrop_right(self):
        return bool(self.get_packet(7)[0] & 0b00000100)

    def wheeldrop_caster(self):
        return bool(self.get_packet(7)[0] & 0b00010000)

    def wall(self):
        return bool(self.get_packet(8)[0])

    def cliff_left(self):
        return bool(self.get_packet(9)[0])

    def cliff_front_left(self):
        return bool(self.get_packet(10)[0])

    def cliff_front_right(self):
        return bool(self.get_packet(11)[0])

    def cliff_right(self):
        return bool(self.get_packet(12)[0])

    def virtual_wall(self):
        return bool(self.get_packet(13)[0])

    def overcurrent_left(self):
        return bool(self.get_packet(14)[0] & 0b00010000)

    def overcurrent_right(self):
        return bool(self.get_packet(14)[0] & 0b00001000)

    def overcurrent_main_brush(self):
        return bool(self.get_packet(14)[0] & 0b00000100)

    def overcurrent_side_brush(self):
        return bool(self.get_packet(14)[0] & 0b00000001)

    def dirt_detect(self):
        return bool(self.get_packet(15))

    def infrared(self):
        return self.get_packet(17)[0]

    def button_dock(self):
        return bool(self.get_packet(18)[0] & 0b00000100)

    def button_spot(self):
        return bool(self.get_packet(18)[0] & 0b00000010)

    def button_clean(self):
        return bool(self.get_packet(18)[0] & 0b00000001)

    def distance(self):
        return struct.unpack(">h", self.get_packet(19, return_bytes=True))[0] * -8

    def angle(self):
        return struct.unpack(">h", self.get_packet(20, return_bytes=True))[0] * 2.75

    def charging_state(self):
        return self.get_packet(21)[0]

    def voltage(self):
        return struct.unpack(">H", self.get_packet(22, return_bytes=True))[0]

    def current(self):
        return struct.unpack(">h", self.get_packet(23, return_bytes=True))[0]

    def battery_temperature(self):
        return struct.unpack(">b", self.get_packet(24, return_bytes=True))[0]

    def battery_charge(self):
        return struct.unpack(">H", self.get_packet(25, return_bytes=True))[0]

    def battery_capacity(self):
        return struct.unpack(">H", self.get_packet(26, return_bytes=True))[0]

    def battery_percentage(self):
        return self.battery_charge()*100 / float(self.battery_capacity())

    def wall_signal(self):
        return struct.unpack(">H", self.get_packet(27, return_bytes=True))[0]

    def cliff_left_signal(self):
        return struct.unpack(">H", self.get_packet(28, return_bytes=True))[0]

    def cliff_front_left_signal(self):
        return struct.unpack(">H", self.get_packet(29, return_bytes=True))[0]

    def cliff_front_right_signal(self):
        return struct.unpack(">H", self.get_packet(30, return_bytes=True))[0]

    def cliff_right(self):
        return struct.unpack(">H", self.get_packet(30, return_bytes=True))[0]
