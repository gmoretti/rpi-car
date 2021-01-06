from gpiozero import Motor
import pygame
import time

motor1 = Motor(27, 17)
motor2 = Motor(24, 23)

def main():
	pygame.init()
	screen = pygame.display.set_mode((640, 480))
	pygame.key.set_repeat(200000)

	clock = pygame.time.Clock()

    
    
	state = 'stopped'

	while True:
		clock.tick(26)
		#pygame.event.pump()
		#pygame.event.wait()
		pressed = pygame.key.get_pressed()

		if pressed[pygame.K_UP] and state != 'forward':
				print('key up pressed')
				motor1.forward()
				motor2.forward()
				state = 'forward'
		elif pressed[pygame.K_DOWN] and state != 'backward':
			
			print('key down pressed')
			motor1.backward()
			motor2.backward()
			state = 'backward'
			
		elif pressed[pygame.K_LEFT] and state != 'left':
			
			print('key left pressed')
			motor1.forward()
			motor2.backward()
			state = 'left'
			
		elif pressed[pygame.K_RIGHT] and state != 'right':
			
			print('key right pressed')
			motor1.backward()
			motor2.forward()
			state = 'right'
			
		elif state != 'stopped' and not pressed[pygame.K_UP] and not pressed[pygame.K_DOWN] and not pressed[pygame.K_LEFT]:
			
			print('key right pressed')
			motor1.stop()
			motor2.stop()
			state = 'stopped'

		for event in pygame.event.get():
			pass

main()
