
__AUTHORS__ = ['Donno', 'Hattiel', 'Shrubber']

import pygame
import engine.snake
import engine.mouse
import random

def renderHud(title):
	fontName = pygame.font.get_default_font()
	font = pygame.font.Font(fontName, 14)
	colour = (0, 0, 255)

	nameSurface = font.render(title, False, colour)
	nameRect = nameSurface.get_rect()
	authorSurface = font.render(', '.join(__AUTHORS__), False, colour)
	authorsY = nameRect.y + nameRect.height + 5
	authorsRect = authorSurface.get_rect()
	authorsRect.y = authorsY
	del authorsY
	offset = 10

	hudRect = (0, 0, 400, 38)
	#hudBackground = pygame.Surface((400, 38))
	#hudBackground.fill(

	def _renderHud(screen):
		nameRect.x = screen.get_rect().width - nameRect.width - offset
		authorsRect.x = screen.get_rect().width - authorsRect.width - offset
		screen.fill( ( 38, 38, 38, 28), hudRect, pygame.BLEND_RGBA_ADD)
		screen.blit(nameSurface, nameRect)
		screen.blit(authorSurface, authorsRect)

	return _renderHud

class Game:
	def __init__(self, title):
		self.title = title
		self.player = engine.snake.Snake((500, 300))
		self.leftPressed = False
		self.rightPressed = False
		self.screenSize = None
		self.mice = []
		

		self.renderhud = renderHud(title)

	def spawnMouse(self):
		# TODO: Write some awesome here to figure out a good place to
		# place the mouse.

		position = (400, 300) if not self.screenSize else (
			random.randint(0, self.screenSize[0]),
			random.randint(0, self.screenSize[1]))

		self.mice.append( engine.mouse.Mouse(*position) )

	def onResize(self, size):
		self.screenSize = size

	def onEvent(self, event):
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				self.leftPressed = True
			if event.key == pygame.K_RIGHT:
				self.rightPressed = True
			if event.key == pygame.K_UP:
				self.player.changespeed(3)
			if event.key == pygame.K_DOWN:
				self.player.changespeed(-3)
			if event.key == pygame.K_s:
				# Spawn a mouse
				self.spawnMouse()
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				self.leftPressed = False
			if event.key == pygame.K_RIGHT:
				self.rightPressed = False
			if event.key == pygame.K_UP:
				self.player.changespeed(-3)
			if event.key == pygame.K_DOWN:
				self.player.changespeed(3)

	def onUpdate(self):
		if self.leftPressed:
			self.player.move(-0.04)
		if self.rightPressed:
			self.player.move(0.04)
		self.player.update(0)

		for mouse in self.mice:
			mouse.update()

	def onRender(self, screen):
		# Clear the whole screen
		screen.fill((0,0,0))

		# Draw the player (snake)
		self.player.draw(screen)

		# Draw the mobs (mice)
		for mouse in self.mice:
			mouse.draw(screen)

		# Render the heads up display
		self.renderhud(screen)
