"""
	Snake - Represents the data for the Snake object.
"""

# Some helper functions and classes for dealing with managing the tail.
import math

class Joint:
	def __init__(self, x, y, distance):
		self.x = x
		self.y = y
		self.distance = distance
		self.rotation = 0

	def updatePosition(self, previousJoint, distance):
		# Calculate the angle.
		dx = self.x - previousJoint.x
		dy = self.y - previousJoint.y
		alpha = math.atan2(dy,dx)

		self.x = int( previousJoint.x + math.cos(alpha) * distance )
		self.y = int( previousJoint.y + math.sin(alpha) * distance )
		self.rotation = math.atan2(
			previousJoint.y-self.y,
			previousJoint.x-self.x) * 180 / math.pi

import pygame
import drawablesnake

def drawSnake(screen, snake):
	screenRect = screen.get_rect()

	head = snake.all_joints[len(snake.all_joints) -1]

	for joint in snake.all_joints:
		if joint == head: continue

		snake.drawSnake.drawBody(screen, (joint.x % screenRect.width, joint.y % screenRect.height), joint.rotation)

	#pygame.draw.rect(screen, (255, 0,0), snake.tail) #, 10, 0)

	x = head.x% screenRect.width
	y = head.y% screenRect.height
	snake.drawSnake.drawHead(screen, (x% screenRect.width, y% screenRect.height), head.rotation, snake.mouthOpen)

	# Disable this circle
	#pygame.draw.circle(screen, (255, 0,0), (x%screenRect.width, y%screenRect.width), 10, 0)

class Snake:
	"""
		A snake has at least two segments the head and the tail.

		The head is the last segment (joint)
	"""

	SegmentDistance = 50

	def __init__(self, position):
		# This includes head, middle and tail.
		self.all_joints = []

		self.drawSnake = drawablesnake.DrawableSnake()

		self.x, self.y = position
		self.new_segment() # Head
		self.new_segment() # Tail

		# The velocity the snake is traveling in X and Y.
		#don't use this
		self.x_velocity = 0
		self.y_velocity = 0
		# The direction the head is travelling
		self.direction = math.pi
		# The current speed
		self.speed = 1
		# the top speed
		self.topspeed = 15

		# The score the snake has.
		self.score = 0

		self.mouthOpen = False

	def new_segment(self):
		self.all_joints.append(Joint(self.x, self.y, Snake.SegmentDistance))

	def remove_segment(self):
		if len(self.all_joints) == 2:
			return # This should be a game over condition...

		self.all_joints.pop()

	def eat_mouse(self, safeToEat):
		if safeToEat:
			# You can't eat a mouse if your mouth is not open.
			if not self.mouthOpen: return
			self.new_segment()
			self.score += 5
		else:
			# You still get damanged by zombie mouse reguardless if you had
			# your mouth open or not.
			self.remove_segment()
			self.score -= 2

	def move(self, theta):
		self.direction += theta

	def changespeed(self, vel):
		if self.speed + vel > 0 and self.speed + vel < self.topspeed:
			self.speed += vel

	def draw(self, screen):
		# Replace this with the correct code / instance
		drawSnake(screen, self)

	def screenResize(self, size):
		self.screenSize = size

	@property
	def mouth(self):
		# screenResize should be called first...
		head = self.all_joints[len(self.all_joints) -1]
		width, height = self.screenSize
		x = head.x% width
		y = head.y% height
		return (x, y)

	@property
	def tail(self):
		# screenResize should be called first...
		tail =  self.all_joints[0]
		width, height = self.screenSize
		x = tail.x % width
		y = tail. y% height
		return pygame.Rect(x-15, y-15, 30, 30) 

	def update(self, timeSinceLastUpdate):
		dx = self.speed*math.cos(self.direction)
		dy = self.speed*math.sin(self.direction)

		self.x += int(math.floor(dx))
		self.y += int(math.floor(dy))

		jointCount = len(self.all_joints)
		for i in xrange(0, jointCount - 1):
			self.all_joints[i].updatePosition(
				self.all_joints[i+1], Snake.SegmentDistance)

		rotation =  (math.pi + math.atan2(
			self.all_joints[jointCount-2].y -self.y ,
			self.all_joints[jointCount-2].x - self.x )) * 180 / math.pi;
		self.all_joints[jointCount-1].x = self.x
		self.all_joints[jointCount-1].y = self.y
		self.all_joints[len(self.all_joints)-1].rotation = rotation
