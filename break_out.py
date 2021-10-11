import pygame
import sys
from random import randint as rand
from math import pi
from simple_ball import Ball

fps = 30

def rand_angle():
  angle = pi/2 + rand(-30, 30)*pi/180
  return angle

class Ball(Ball):
  def collide(self, pf):
    x = self.geometry.x
    y = self.geometry.y
    if y + self.radius >= pf.y - pf.h:
      if pf.x <= x <= pf.x + pf.w:
        self.move_y = -self.move_y

class Platform():
  def __init__(self, screen):
    self.size = pygame.display.get_surface().get_size()
    self.w, self.h = 80, 10
    self.x = self.size[0]/2 - self.w/2
    self.y = self.size[1]*0.9
    self.collor = (50, 255, 50)
    self.turns = 0
    self.speed = 3
  
  def moves(self):
    self.x += self.speed * self.turns
    if not 0 <= self.x <= self.size[0] - self.w:
      if self.x < 0:
        self.x = 0
      else: self.x = self.size[0] - self.w
  
  def turn(self, t):
    if t == 1:
      self.turns = 1
    elif t == -1: self.turns = -1
    else: self.turns = 0

  def draw(self, screen):
    pygame.draw.rect(screen, self.collor, (self.x, self.y, self.w, self.h))

def break_out():
  size = width, height = 800, 600
  pygame.init()
  pygame.display.set_caption('BreakOut')
  screen = pygame.display.set_mode(size, pygame.RESIZABLE)

  BLACK = 0, 0, 0

  ball = Ball(screen)
  pf = Platform(screen)

  game_over = False
  while not game_over:
    # события
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        game_over = True
      
      if event.type == pygame.VIDEORESIZE:
        size = width, height = event.w, event.h
        screen = pygame.display.set_mode(size, pygame.RESIZABLE)
      
      if event.type == pygame.KEYDOWN:
        if pygame.K_a == event.key:
          pf.turn(-1)
        
        if pygame.K_d == event.key:
          pf.turn(1)
      
      if event.type == pygame.KEYUP:
        if pygame.K_a == event.key or pygame.K_d == event.key:
          pf.turn(0)
    
    # логика работы игры
    ball.collide(pf)
    ball.move()
    pf.moves()

    # отрисовка
    screen.fill(BLACK)
    ball.draw(screen)
    pf.draw(screen)

    pygame.display.flip()

    # подождать
    pygame.time.wait(fps)
    
  sys.exit()


if __name__ == '__main__':
  break_out()
