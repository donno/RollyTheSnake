import pygame

import os.path

def path(*args):
	"""Helper function for returning the path to an asset"""
	# Example: path('subfolder', 'image.jpg')	
	return os.path.join('assets', *args)

class DrawableSnake:
	def __init__(self):
		self.headImage = pygame.image.load(path('head.png'))
		self.middleImage = pygame.image.load(path('middle.png'))

		self.headImages = {}
		for degree in xrange(0, 360, 4):
			self.headImages[degree] = pygame.transform.rotate(self.headImage, degree )
			if degree < 90 or degree < 270:
				self.headImages[degree] = pygame.transform.flip(self.headImages[degree], True, False)
			elif degree > 270:
				image = pygame.transform.flip(self.headImages[degree], True, False)
				self.headImages[degree] = pygame.transform.rotate(image, degree )


		self.middleImages = {}
		for degree in xrange(0, 360, 4):		
			self.middleImages[degree] = pygame.transform.rotate(self.middleImage, degree )
			if degree < 90 or degree < 270:
				self.middleImages[degree] = pygame.transform.flip(self.middleImages[degree], True, False)
			elif degree > 270:
				self.middleImages[degree] = pygame.transform.flip(self.middleImages[degree], False, True)


	def drawHead(self, screen, position, rotation):
		rotation = int(rotation) -  int(rotation) % 4

		image = self.headImages[rotation % 360]

		imageRect = image.get_rect()
		x, y = position
		dest = pygame.Rect(x - imageRect.center[0], y - imageRect.center[1],
			imageRect.width, imageRect.height)

		screen.blit(image, dest)

	def drawBody(self, screen, position, rotation):
		rotation = int(rotation) -  int(rotation) % 4

		image = self.middleImages[rotation % 360]

		imageRect = image.get_rect()
		x, y = position
		dest = pygame.Rect(x - imageRect.center[0], y - imageRect.center[1],
			imageRect.width, imageRect.height)

		screen.blit(image, dest)
