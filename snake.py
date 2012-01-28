import pygame

import os.path

def path(*args):
	"""Helper function for returning the path to an asset"""
	# Example: path('subfolder', 'image.jpg')	
	return os.path.join('assets', *args)


class Snake(pygame.sprite.Group):
	def __init__(self):
		pygame.sprite.Group.__init__(self)

		# Create the head.
		self.head = pygame.sprite.Sprite()
		self.head.imageToRight = pygame.image.load(path('head.png'))
		self.head.imageToLeft = pygame.transform.flip(self.head.imageToRight, True, False)
		self.head.image = self.head.imageToLeft
		self.head.rect = self.head.image.get_rect()
		# Create the tail.
		self.tail = pygame.sprite.Sprite()
		self.tail.imageToRight = pygame.image.load(path('end.png'))
		self.tail.imageToLeft = pygame.transform.flip(self.tail.imageToRight, True, False)
		self.tail.image = self.tail.imageToLeft
		self.tail.rect = self.tail.image.get_rect()

		self.add(self.tail)
		self.add(self.head)

		self.tail.x_offset = 22
		#self.tail.rect.left += self.head.rect.width - self.tail.x_offset
		self.tail.rect.left = self.head.rect.left - self.head.rect.width + self.tail.x_offset
		self.tail.rect.top += 16

		#self.image = pygame.Surface([50,20])
		#self.image.fill((0,255,0))
		self.rect = self.head.image.get_rect()
		initPos = [100,100]
		self.rect.topleft = initPos
		self.x_speed = 0
		self.y_speed = 0

	def draw(self, screen):
		pygame.sprite.RenderPlain((self)).draw(screen) #magic

	def move(self, x, y):
		oldSpeed = -self.x_speed
		self.x_speed += x
		self.y_speed += y
		# TODO: Figure out how to flip the entire group.

		if self.x_speed > 0:
			self.head.image = self.head.imageToLeft
			self.tail.image = self.tail.imageToLeft
			self.tail.rect.left = self.head.rect.left - self.head.rect.width + self.tail.x_offset
		elif self.x_speed < 0:
			self.head.image = self.head.imageToRight
			self.tail.image = self.tail.imageToRight
			self.tail.rect.left = self.head.rect.right - self.tail.x_offset


	def update(self, timeSinceLastUpdate):
		self.rect.top += self.y_speed
		self.rect.left += self.x_speed


		for sprite in self.sprites():
			sprite.rect.top += self.y_speed
			sprite.rect.left += self.x_speed
