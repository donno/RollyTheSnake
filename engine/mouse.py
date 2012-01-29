
import math
import random
import pygame

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
        size = 20
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

    # The Mouse class is abstract as such children of this class are
    # responsible of providing the draw method.
    # def draw(self, screen):

class MouseNormal(Mouse):
    SafeToEat = True
    def __init__(self, x, y):
        #Mouse.__init__(self, x, y)
        self.direction = 0
        self.running = False
        self.runDist = 0

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), 10, 0)

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
    def __init__(self, x, y):
        Mouse.__init__(self, x, y)

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 0, 255), (self.x, self.y), 10, 0)

    def update(self):
        pass

