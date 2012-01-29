
__AUTHORS__ = ['Donno', 'Hattiel', 'Shrubber']

import pygame
import engine.snake
import engine.mouse
import random

class Hud:
	def __init__(self, title):
		fontName = pygame.font.get_default_font()
		font = pygame.font.Font(fontName, 14)
		colour = (0, 0, 255)

		self.nameSurface = font.render(title, False, colour)
		self.nameRect = self.nameSurface.get_rect()
		self.authorSurface = font.render(', '.join(__AUTHORS__), False, colour)
		authorsY = self.nameRect.y + self.nameRect.height + 5
		self.authorsRect = self.authorSurface.get_rect()
		self.authorsRect.y = authorsY

		self.hudRect = (0, 0, 400, 38)
		self.scoreFont = font = pygame.font.Font(fontName, 28)

	# Could add an update method...

	def draw(self, screen, score):
		offset = 10
		self.nameRect.x = screen.get_rect().width - self.nameRect.width - offset
		self.authorsRect.x = screen.get_rect().width - self.authorsRect.width - offset
		screen.fill(
			( 38, 38, 38, 28),
			self.hudRect,
			pygame.BLEND_RGBA_ADD)

		scoreSurface = self.scoreFont.render('Score: %d' % score, False, (240,240,240))
		# Could add some padding around the score.
		screen.blit(scoreSurface, scoreSurface.get_rect())
		screen.blit(self.nameSurface, self.nameRect)
		screen.blit(self.authorSurface, self.authorsRect)

class Game:
	def __init__(self, title):
		self.title = title
		self.player = engine.snake.Snake((500, 300))
		self.leftPressed = False
		self.rightPressed = False
		self.screenSize = None
		self.mice = []

		self.hud = Hud(title)

	def spawnMouse(self):
		# TODO: Write some awesome here to figure out a good place to
		# place the mouse.

		position = (400, 300) if not self.screenSize else (
			random.randint(50, self.screenSize[0]-50),
			random.randint(50, self.screenSize[1]-50))

		self.mice.append( engine.mouse.Mouse(*position) )

	def onResize(self, size):
		self.screenSize = size
		self.player.screenResize(size)

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
			if event.key == pygame.K_SPACE:
				# Open the snakes mouth.
				if not self.player.mouthOpen:
					self.player.mouthOpen = True
					self.mouthTimeOut = 20
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

		self.check_mice()

		if self.player.mouthOpen:
			self.mouthTimeOut -= 1
			if self.mouthTimeOut == 0:
				self.player.mouthOpen = False

	def onRender(self, screen):
		# Clear the whole screen
		screen.fill((0,0,0))

		# Draw the player (snake)
		self.player.draw(screen)

		# Draw the mobs (mice)
		for mouse in self.mice:
			mouse.draw(screen)

		# Render the heads up display
		self.hud.draw(screen, self.player.score)

	# Check if the snake is colliding with any mice.
	def check_mice(self):
		aliveMice = []
		for mouse in self.mice:
			# Test if its colliding with the nose of the snake.
			if mouse.rect.collidepoint(self.player.mouth):
				# TODO: Handle zombie mouse.
				self.player.eat_mouse(safeToEat=mouse.SafeToEat)
			else:
				# This mouse is still alive.
				aliveMice.append(mouse)
		self.mice = aliveMice
