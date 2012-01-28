import pygame

import os.path

def path(*args):
	"""Helper function for returning the path to an asset"""
	# Example: path('subfolder', 'image.jpg')	
	return os.path.join('assets', *args)

class DrawableSnake:
	def __init__(self):
		self.headImage = pygame.image.load(path('head.png'))

		self.headImages = {}
		for degree in xrange(0, 360, 4):
			self.headImages[degree] = pygame.transform.rotate(self.headImage, degree )

	def drawHead(self, screen, position, rotation):

		
		rotation = int(rotation) -  int(rotation) % 4

		image = self.headImages[rotation % 360]

		imageRect = image.get_rect()
		x, y = position
		dest = pygame.Rect(x - imageRect.center[0], y - imageRect.center[1],
			imageRect.width, imageRect.height)

		print rotation
		screen.blit(image, dest)

		# Draw  image.center

	
