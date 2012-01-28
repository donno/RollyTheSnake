
import pygame
import snake

import engine.snake

class Game:
	def __init__(self):
		#self.player = snake.Snake()
                self.player = engine.snake.Snake((100, 100))


	def onEvent(self, event):
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                                self.player.move(0.5)
                        if event.key == pygame.K_RIGHT:
                                self.player.move(-0.5)
                        if event.key == pygame.K_UP:
                                self.player.changespeed(3)
                        if event.key == pygame.K_DOWN:
                                self.player.changespeed(-3)
                elif event.type == pygame.KEYUP:
                        if event.key == pygame.K_LEFT:
                                self.player.move(-0.5)
                        if event.key == pygame.K_RIGHT:
                                self.player.move(0.5)
                        if event.key == pygame.K_UP:
                                self.player.changespeed(-3)
                        if event.key == pygame.K_DOWN:
                                self.player.changespeed(3)
		
        def onUpdate(self):
                self.player.update(0)
                #self.newPlayer.update(0)

	def onRender(self, screen):
		screen.fill((0,0,0))
		self.player.draw(screen)	
                #self.newPlayer.draw(screen)
