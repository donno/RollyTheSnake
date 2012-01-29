
import math
import random
import pygame

import os.path

def path(*args):
	"""Helper function for returning the path to an asset"""
	# Example: path('subfolder', 'image.jpg')
	return os.path.join('assets', *args)

def determineType():
    # Mouse weighting
    chances = {
        'normal' : (0.6, Mouse.Normal),
        'zombie' : (0.4, Mouse.Zombie),
        }

    assert len(chances) < 100
    options = []
    for name, data in chances.iteritems():
        perctange, typeid = data

        for i in xrange(0, int(perctange * 100)):
            options.append(typeid)

    return random.choice(options)

class Mouse:

    # Enumeration of mouse types.
    Normal = 0
    Zombie = 1

    @property
    def rect(self):
        size = self.image.get_rect().width - 3 # 3 for the transparency
        return pygame.Rect(self.x - size, self.y - size/2, size, size)

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = determineType()

        mouseTypes = {
            Mouse.Normal : MouseNormal,
            Mouse.Zombie : MouseZombie,
            }

        self.__class__ = mouseTypes[self.type]
        self.__class__.__init__(self, x, y)

    def update(self):
        #self.updateFunction(self)
        pass

    def draw(self, screen):
        if not self.image: return

        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), 10, 0)

        imageRect = self.image.get_rect()
        dest = pygame.Rect(self.x - imageRect.center[0], self.y - imageRect.center[1],
            imageRect.width, imageRect.height)
        screen.blit(self.image, dest)

class MouseNormal(Mouse):
    SafeToEat = True
    
    Image1 = pygame.image.load(path('mouse1.png')) 
    Image2 = pygame.image.load(path('mouse2.png')) 

    def __init__(self, x, y):
        #Mouse.__init__(self, x, y)
        self.direction = 0
        self.running = False
        self.runDist = 0
        self.image = random.choice([self.Image1, self.Image2])

    def update(self):
        if random.randint(0,150) == 1:
            self.direction = (math.pi/180)*(random.randrange(0,359))
            self.running = True
        if self.running:
            dx = int(5*math.cos(self.direction))
            dy = int(5*math.sin(self.direction))
            if self.x + dx > 50 and self.x +dx < 1024 - 50 :   #hard coded screen size
                if self.y + dy > 50 and self.y +dy < 600 - 50 :   #hard coded screen size
                    self.x += dx
                    self.y += dy
            self.runDist += 10
            if self.runDist > 150:
                self.running = False
                self.runDist = 0

class MouseZombie(Mouse):
    SafeToEat = False
    
    Image1 = pygame.image.load(path('zmouse1.png')) 
    Image2 = pygame.image.load(path('zmouse2.png')) 

    def __init__(self, x, y):
        self.image = random.choice([self.Image1, self.Image2])
        self.direction = 0
        self.running = False
        self.runDist = 0

    def update(self):
        if random.randint(0,150) == 1:
            self.direction = (math.pi/180)*(random.randrange(0,359))
            self.running = True
        if self.running:
            dx = int(5*math.cos(self.direction))
            dy = int(5*math.sin(self.direction))
            if self.x + dx > 50 and self.x +dx < 1024 - 50 :   #hard coded screen size
                if self.y + dy > 50 and self.y +dy < 600 - 50 :   #hard coded screen size
                    self.x += dx
                    self.y += dy
            self.runDist += 10
            if self.runDist > 150:
                self.running = False
                self.runDist = 0

