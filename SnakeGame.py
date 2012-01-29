import pygame

from game import Game

__NAME__ = 'Rolly the Snake'
__AUTHORS__ = ['Donno', 'Hattiel', 'Shrubber']

SCREEN_SIZE = 1024, 600

def main():
	pygame.init()
	pygame.font.init()

	game = Game(__NAME__)
	size = SCREEN_SIZE
	screen = pygame.display.set_mode(size)
	pygame.display.set_caption(__NAME__)
	isRunning = True
	clock = pygame.time.Clock()
	game.onResize(size)
	while isRunning:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				isRunning = False
				break
			game.onEvent(event)

		game.onUpdate()
		game.onRender(screen)
		pygame.display.flip()
		clock.tick(100)

	pygame.quit()

if __name__ == '__main__':
	main()

