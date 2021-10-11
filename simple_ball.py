import pygame
import sys
from random import randint as rand
from math import pi, cos, sin

fps = 30

def rand_angle():
  sign = -1 if rand(0, 1) == 0 else 1
  angle = pi/2 + sign * rand(30, 90)*pi/180
  return angle

class Ball():
  def __init__(self, screen, angle=rand_angle()):
    self.size = pygame.display.get_surface().get_size()
    self.image = pygame.image.load('basketball.png')
    self.radius = 13
    self.image = pygame.transform.scale(self.image, (self.radius*2, self.radius*2))
    self.geometry = self.image.get_rect()
    self.geometry.centerx = self.size[0]/2
    self.geometry.centery = self.size[1]*0.8
    self.move_x = cos(angle)
    self.move_y = -sin(angle)
    self.speed = 4

  def draw(self, screen):
    screen.blit(self.image, self.geometry)
  
  def move(self):
    if 0 >= self.geometry.centerx - self.radius:
      self.move_x = -self.move_x
      self.geometry.x += 2
    elif self.size[0] <= self.geometry.centerx + self.radius:
      self.move_x = -self.move_x
      self.geometry.x -= 2

    if 0 >= self.geometry.y:
      self.move_y = -self.move_y
      self.geometry.y += 2
    
    self.geometry.centerx += self.move_x * self.speed
    self.geometry.centery += self.move_y * self.speed

def simple_ball():
  size = width, height = 800, 600
  pygame.init()
  pygame.display.set_caption('BreakOut')
  screen = pygame.display.set_mode(size, pygame.RESIZABLE)

  BLACK = 0, 0, 0

  ball = Ball(screen)

  game_over = False
  while not game_over:
    # события
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        game_over = True
      
      if event.type == pygame.VIDEORESIZE:
        size = width, height = event.w, event.h
        screen = pygame.display.set_mode(size, pygame.RESIZABLE)
    
    # логика работы игры
    ball.move()

    # отрисовка
    screen.fill(BLACK)
    ball.draw(screen)

    pygame.display.flip()

    # подождать
    pygame.time.wait(fps)
    
  sys.exit()

if __name__ == '__main__':
    simple_ball()
