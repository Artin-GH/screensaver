import pygame
import random

screen_width, screen_height = (800, 600)
screen_size = (screen_width, screen_height)
fps = 60

pygame.init()
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Screensaver (Project - X)')

class Square:
	def __init__(self, color, pos, size, side):
		self.color = color
		self.pos = list(pos)
		self.size = size
		self.side_x, self.side_y = side
		self.speed = 1

running = True
square_count = 400
square_size = 3
squares = []
font = pygame.font.SysFont('helvetica', 45)

for i in range(square_count):
	x = random.randint(0, screen_width - square_size)
	y = random.randint(0, screen_height - square_size)
	squares.append(Square([random.randint(1, 255) for i in range(3)], [x, y], square_size, [random.choice([-1, 1]) for i in range(2)]))

while running:
	screen.fill((0, 0, 0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	for square in squares:
		pygame.draw.rect(screen, square.color, pygame.Rect(*square.pos, *([square.size] * 2)))
		square.pos[0] += square.side_x * square.speed
		square.pos[1] += square.side_y * square.speed
		if square.pos[0] + square.size >= screen_width or square.pos[0] <= 0:
			square.side_x *= -1
		if square.pos[1] + square.size >= screen_height or square.pos[1] <= 0:
			square.side_y *= -1
		for sqr in squares:
			if sqr != square:
				if (square.pos[0] + square.size >= sqr.pos[0] and square.pos[0] <= sqr.pos[0] + sqr.size) and (square.pos[1] + square.size >= sqr.pos[1] and square.pos[1] <= sqr.pos[1] + sqr.size):
					square.side_x *= sqr.side_x
					square.side_y *= sqr.side_y
	pygame.display.update()
