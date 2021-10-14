import pygame
from simple_ball import Ball

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
