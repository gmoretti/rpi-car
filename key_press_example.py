import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    pygame.key.set_repeat(0)

    while True:
                
        pressed = pygame.key.get_pressed()

        for event in pygame.event.get():
            if pressed[pygame.K_UP]: print('key up pressed')
            else:
                print("nothing")

            
            # determin if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                # determine if a letter key was pressed
                if event.key == pygame.K_w:
                    print('w pressed')
                elif event.key == pygame.K_s:
                    print('s pressed')

            if event.type == pygame.KEYUP:
                print('released')
                
            clock.tick(60)

main()
