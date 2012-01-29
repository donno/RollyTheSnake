
import math
import random
import pygame

def normalMouseUpdate(mouse):
    mouse.x += random.randint(-6, 6)
    mouse.y += random.randint(-6, 6)


def zombieMouseUpdate(mouse):
    pass

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

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = determineType()

        mouseTypes = {
            Mouse.Normal : MouseNormal,
            Mouse.Zombie : MouseZombie,
            }

        self.__class__ = mouseTypes[self.type]
        #self. = Mouse.MoveMap[self.type]

    def update(self):
        #self.updateFunction(self)
        pass

    # The Mouse class is abstract as such children of this class are
    # responsible of providing the draw method.
    # def draw(self, screen):

class MouseNormal(Mouse):
    def __init__(self, x, y):
        Mouse.__init__(self, x, y)
        self.direction = 0
        self.running = False
        self.runDist = 0

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), 10, 0)

    def update(self):
        if random.randint(0,150) == 1:
            self.direction = random.randrange(0,2*math.pi)
            self.running = True
        if self.running:
            dx = int(10*math.cos(self.direction))
            dy = int(10*math.sin(self.direction))
            if self.x + dx > 50 and self.x +dx < 1024 - 50 :   #hard coded screen size
                self.x += dx
            if self.y + dy > 50 and self.y +dy < 600 - 50 :   #hard coded screen size
                self.y += dy

class MouseZombie(Mouse):
    def __init__(self, x, y):
        Mouse.__init__(self, x, y)

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 0, 255), (self.x, self.y), 10, 0)

    def update(self):

