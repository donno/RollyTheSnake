"""
	Snake - Represents the data for the Snake object.
"""

# Some helper functions and classes for dealing with managing the tail.
import math

def getPosition(origin, destination, distance):
	# Calc Angle
	dx = destination.x - origin.x;
	dy = destination.y - origin.y;
	alpha = math.atan2(dy,dx);
	#rotation = ( math.pi + alpha ) * 180 / math.pi
	rotation = math.atan2(origin.y-destination.y, origin.x-destination.x) * 180 / math.pi

	# Returns the new postion and the rotation.
	return (
		int( origin.x + math.cos(alpha) * distance ),
		int( origin.y + math.sin(alpha) * distance ),
		rotation
		)

class Joint:
	def __init__(self, x, y, distance):
		self.x = x
		self.y = y
		self.distance = distance
		self.rotation = 0

	def setPosition(self, position):
		self.x, self.y, self.rotation = position

import pygame
import drawablesnake

def drawSnake(screen, snake):
	screenRect = screen.get_rect()

	head = snake.all_joints[len(snake.all_joints) -1]

	for joint in snake.all_joints:
		if joint == head: continue

		pygame.draw.circle(screen, (0, 255,0), (joint.x, joint.y), 10, 0)
		snake.drawSnake.drawBody(screen, (joint.x % screenRect.width, joint.y % screenRect.height), joint.rotation)

	pygame.draw.circle(screen, (255, 0,0), (head.x, head.y), 10, 0)
	snake.drawSnake.drawHead(screen, (head.x% screenRect.width, head.y% screenRect.height), head.rotation)


class Snake:
	"""
		A snake has at least two segments the head and the tail.

		The head is the last segment (joint)
	"""

	SegmentDistance = 50

	def __init__(self, position):
		# This includes head, segements and tail.
		self.all_joints = []

		self.drawSnake = drawablesnake.DrawableSnake()

		self.x, self.y = position
		self.new_segment()
		for x in xrange(0, 9):
			self.new_segment()

		# The segments that build up the head to the tail.
		self.segments = []

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

	def new_segment(self):
		self.all_joints.append(Joint(self.x, self.y, Snake.SegmentDistance))

	def move(self, theta):
		self.direction += theta

	def changespeed(self, vel):
		if self.speed + vel > 0 and self.speed + vel < self.topspeed:
			self.speed += vel

	def draw(self, screen):
		# Replace this with the correct code / instance
		drawSnake(screen, self)

	def update(self, timeSinceLastUpdate):
		dx = self.speed*math.cos(self.direction)
		dy = self.speed*math.sin(self.direction)

		self.x += int(math.floor(dx))
		self.y += int(math.floor(dy))

		jointCount = len(self.all_joints)
		for i in xrange(0, jointCount - 1):
			self.all_joints[i].setPosition(getPosition(self.all_joints[i+1], self.all_joints[i], Snake.SegmentDistance))

		rotation =  (math.pi + math.atan2(
			self.all_joints[jointCount-2].y -self.y ,
			self.all_joints[jointCount-2].x - self.x )) * 180 / math.pi;
		self.all_joints[jointCount-1].x = self.x
		self.all_joints[jointCount-1].y = self.y
		self.all_joints[len(self.all_joints)-1].rotation = rotation
