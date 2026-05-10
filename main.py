import pygame
print('setup start')
pygame.init()
window = pygame.display.set_mode(size=(600, 400))
print('setup End')

print('loop Start')
while True:
    # check for all events
   for event in pygame.event.get():
       if event.type ==pygame.QUIT:
          pygame.quit() #close window
          quit() #end pygame




