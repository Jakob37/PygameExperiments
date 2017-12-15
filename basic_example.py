#!/usr/bin/env python3


import pygame
import os

os.putenv('SDL_FBDEV', '/dev/fb1')

pygame.init()

lcd = pygame.display.set_mode((320, 240))
lcd.fill((255, 0, 0))

pygame.display.update()

pygame.mouse.set_visible(False)

lcd.fill((0,0,0))

while True:
	pygame.display.update()

	
	for event in pygame.event.get():

		if event.type == KEYDOWN:
			print("Exit game!")
			sys.exit(0)



