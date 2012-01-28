import pygame

from game import Game

__NAME__ = 'Rolly the Snake'
__AUTHORS__ = ['Donno', 'Hattiel', 'Shrubber']

SCREEN_SIZE = 1024, 600

def renderHud():
	fontName = pygame.font.get_default_font()
	font = pygame.font.Font(fontName, 14)
	colour = (0, 0, 255)

	nameSurface = font.render(__NAME__, False, colour)
	nameRect = nameSurface.get_rect()
	authorSurface = font.render(', '.join(__AUTHORS__), False, colour)
	authorsY = nameRect.y + nameRect.height + 5
	authorsRect = authorSurface.get_rect()
	authorsRect.y = authorsY
	del authorsY
	offset = 10

	def _renderHub(screen):
		nameRect.x = screen.get_rect().width - nameRect.width - offset
		authorsRect.x = screen.get_rect().width - authorsRect.width - offset
		screen.blit(nameSurface, nameRect)
		screen.blit(authorSurface, authorsRect)

	return _renderHub

def main():
	pygame.init()
	pygame.font.init()

	game = Game()
	size = SCREEN_SIZE
	screen = pygame.display.set_mode(size)
	pygame.display.set_caption(__NAME__)
	isRunning = True
	renderhud = renderHud()
	while isRunning:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				isRunning = False
				break
			game.onEvent(event)

		renderhud(screen)
		game.onRender(screen)
		pygame.display.flip()

	pygame.quit()

if __name__ == '__main__':
	main()

