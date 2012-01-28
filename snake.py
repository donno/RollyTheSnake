import pygame

import os.path

def path(*args):
	"""Helper function for returning the path to an asset"""
	# Example: path('subfolder', 'image.jpg')	
	return os.path.join('assets', *args)


class Snake(pygame.sprite.Group):
	Gravity = 9.8 # ms or maybe change to px per tick...

	def __init__(self):
		pygame.sprite.Group.__init__(self)

		# Create the head.
		self.head = pygame.sprite.Sprite()
		self.head.imageToRight = pygame.image.load(path('head.png'))
		self.head.imageToLeft = pygame.transform.flip(self.head.imageToRight, True, False)
		self.head.image = self.head.imageToLeft
		self.head.rect = self.head.image.get_rect()

		# Load in the middle graphics.
		self.middleImageToRight = pygame.image.load(path('middle.png'))
		self.middleImageToLeft = pygame.transform.flip(self.middleImageToRight, True, False)

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

		self.middles = []

		# TODO: Fix this as its wrong it doesn't take into consideration
		self.rect = self.head.image.get_rect()
		initPos = [100,100]
		self.rect.topleft = initPos
		self.x_speed = 0
		self.y_speed = 0

		self.addMiddle()
		self.addMiddle()

	def draw(self, screen):
		pygame.sprite.RenderPlain((self)).draw(screen) #magic

	def addMiddle(self):
		# Add me.
		newMiddle = pygame.sprite.Sprite()
		newMiddle.image = self.middleImageToLeft
		newMiddle.rect = newMiddle.image.get_rect()
		newMiddle.rect.top += 14
		newMiddle.imageToLeft = self.middleImageToLeft
		newMiddle.imageToRight = self.middleImageToRight
		newMiddle.rect.left -=  self.head.rect.width

		if len(self.middles) == 0:
			# Off set
			self.tail.rect.top += 10

		self.middles.append(newMiddle) 
		self.remove(self.head)
		self.add(newMiddle)
		self.add(self.head)



	def move(self, x, y):
		oldSpeed = -self.x_speed
		self.x_speed += x
		self.y_speed += y
		# TODO: Figure out how to flip the entire group.

		middleOffset = 18
		if self.x_speed > 0:
			
			for sprite in self.sprites():
				sprite.image = sprite.imageToLeft


			newX = self.head.rect.left 
			for middle in self.middles:
				middle.rect.right = newX + middleOffset 
				newX = middle.rect.right - middle.rect.width

			self.tail.rect.right = newX + self.tail.x_offset
			
		elif self.x_speed < 0:
			for sprite in self.sprites():
				sprite.image = sprite.imageToRight

			lastX = self.head.rect.right - self.tail.x_offset
			for middle in self.middles:
				middle.rect.left = lastX 
				lastX += middle.rect.width - middleOffset + 11
			
			self.tail.rect.left = lastX - self.tail.x_offset

	def update(self, timeSinceLastUpdate):
		self.rect.top += self.y_speed
		self.rect.left += self.x_speed

		for sprite in self.sprites():
			sprite.rect.top += self.y_speed
			sprite.rect.left += self.x_speed
