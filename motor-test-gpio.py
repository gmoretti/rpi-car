from gpiozero import Motor
import time

motor1 = Motor(27, 17)
motor2 = Motor(24, 23)

print('going forward')
motor1.forward()
motor2.forward()

time.sleep(2)

print('going backward')
motor1.backward()
motor2.backward()

time.sleep(2)

print('stopping')

motor1.stop()
motor2.stop()

time.sleep(2)
