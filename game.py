
import pygame
import snake

class Game:
	def __init__(self):
		self.player = snake.Snake()

	def onEvent(self, event):
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                                self.player.move(-3,0)
                        if event.key == pygame.K_RIGHT:
                                self.player.move(3,0)
                        if event.key == pygame.K_UP:
                                self.player.move(0,-3)
                        if event.key == pygame.K_DOWN:
                                self.player.move(0,3)
                if event.type == pygame.KEYUP:
                        if event.key == pygame.K_LEFT:
                                self.player.move(3,0)
                        if event.key == pygame.K_RIGHT:
                                self.player.move(-3,0)
                        if event.key == pygame.K_UP:
                                self.player.move(0,3)
                        if event.key == pygame.K_DOWN:
                                self.player.move(0,-3)
		self.player.update(0)

	def onRender(self, screen):
		screen.fill((0,0,0))
		self.player.draw(screen)	
