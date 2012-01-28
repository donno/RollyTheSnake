
import snake

class Game:
	def __init__(self):
		self.player = snake.Snake()

	def onEvent(self, event):
		pass

	def onRender(self, screen):
		self.player.draw(screen)	
