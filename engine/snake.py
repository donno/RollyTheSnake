"""
	Snake - Represents the data for the Snake object.
"""

import math

import drawablesnake

def getPosition(origin, destination, distance):
	# Calc Angle
	dx = destination.x - origin.x;
	dy = destination.y - origin.y;
	alpha = math.atan2(dy,dx);
	rotation = ( math.pi + alpha ) * 180 / math.pi;
	
	# New Pos at set distance
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

def drawSnake(screen, snake):

	for joint in snake.all_joints:
		pygame.draw.circle(screen, (0, 255,0), (joint.x, joint.y), 10, 0)


	head = snake.all_joints[len(snake.all_joints) -1]
	pygame.draw.circle(screen, (255, 0,0), (head.x, head.y), 10, 0)
	snake.drawSnake.drawHead(screen, (head.x, head.y), head.rotation)


class Snake:
	"""
		A snake has at least two components: the head and the tail.

	"""

	SegmentDistance = 60

	def __init__(self, position):
		# This includes head, segements and tail.
		self.all_joints = []

		self.drawSnake = drawablesnake.DrawableSnake()

		self.x, self.y = position
		self.new_segment()
		for x in xrange(0, 20):
			self.new_segment()

		# The segments that build up the head to the tail.
		self.segments = []

		# The velocity the snake is traveling in X and Y.
		self.x_velocity = 0
		self.y_velocity = 0

	def new_segment(self):
		self.all_joints.append(Joint(self.x, self.y, Snake.SegmentDistance))

	def move(self, x, y):
		self.x_velocity += x
		self.y_velocity += y


	def draw(self, screen):
		# Replace this with the correct code / instance
		drawSnake(screen, self)

	def update(self, timeSinceLastUpdate):
		self.x += self.x_velocity
		self.y += self.y_velocity



		jointCount = len(self.all_joints)
		for i in xrange(0, jointCount - 1):
			self.all_joints[i].setPosition(getPosition(self.all_joints[i+1], self.all_joints[i], Snake.SegmentDistance))


		rotation =  (math.pi + math.atan2(
			self.all_joints[jointCount-2].y -self.y ,
			self.all_joints[jointCount-2].x - self.x )) * 180 / math.pi;
		self.all_joints[jointCount-1].x = self.x
		self.all_joints[jointCount-1].y = self.y
		self.all_joints[len(self.all_joints)-1].rotation = rotation
