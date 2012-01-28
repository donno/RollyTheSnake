import pygame

import os.path

def path(*args):
	"""Helper function for returning the path to an asset"""
	# Example: path('subfolder', 'image.jpg')	
	return os.path.join('assets', *args)


class Snake(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.imageFor = pygame.image.load(path('head.png'))
		self.imageRev = pygame.transform.flip(self.imageFor, True, False)
		self.image = self.imageFor
		#self.image = pygame.Surface([50,20])
		#self.image.fill((0,255,0))
		self.rect = self.image.get_rect()
		initPos = [100,100]
		self.rect.topleft = initPos
		self.x_speed = 0
		self.y_speed = 0

	def draw(self, screen):
		pygame.sprite.RenderPlain((self)).draw(screen) #magic

	def move(self, x, y):
		self.x_speed += x
		self.y_speed += y
		if (self.x_speed > 0):
			self.image = self.imageRev
		elif self.x_speed < 0:
			self.image = self.imageFor

	def update(self, timeSinceLastUpdate):
		self.rect.top += self.y_speed
		self.rect.left += self.x_speed
