
import pygame
import engine.snake
import engine.mouse
import random

class Game:
	def __init__(self):
		self.player = engine.snake.Snake((500, 300))
		self.leftPressed = False
		self.rightPressed = False
		self.screenSize = None
		self.mice = []

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
		screen.fill((0,0,0))
		self.player.draw(screen)

		for mouse in self.mice:
			mouse.draw(screen)
