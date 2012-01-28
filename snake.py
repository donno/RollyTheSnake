import pygame

class Snake(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([50,20])
		self.image.fill((0,255,0))
		self.rect = self.image.get_rect()
		initPos = [100,100]
		self.rect.topleft = initPos
		self.x_speed = 0
		self.y_speed = 0
"""
	def draw(self, screen):
		pygame.sprite.RenderPlain((self)).draw(screen) #magic
		pygame.display.flip()
"""
	def move(self, x, y):
		self.x_speed += x
		self.y_speed += y


	def update(self, timeSinceLastUpdate):
		self.rect.top += self.y_speed
		self.rect.left += self.x_speed

