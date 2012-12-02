from main import Roomba
import time

print "Opening connection"
roomba = Roomba("/dev/ttyAMA0", 115200)
print "Done"

time.sleep(1)

left_state = -1
right_state = -1
while 1:
    new_left_state = roomba.sensors.bumper_left
    new_right_state = roomba.sensors.bumper_right
    if new_left_state != left_state:
        if new_left_state:
            print 'Left bumper is pressed'
        else:
            print 'Left bumper is released'
        if new_right_state != right_state:
            if new_right_state:
                print 'Right bumper is pressed'
            else:
                print 'Right bumper is released'
    left_state = new_left_state
    right_state = new_right_state
    time.sleep(0.1)
