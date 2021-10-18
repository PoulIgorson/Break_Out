import pygame
from random import randint as rand
from math import pi, cos, sin

def rand_angle():
  sign = -1 if rand(0, 1) == 0 else 1
  angle = pi/2 + sign * rand(1, 60)*pi/180
  return angle

class Ball():
  def __init__(self, screen, angle=rand_angle()):
    self.size = pygame.display.get_surface().get_size()
    self.image = pygame.image.load('basketball.png')
    self.radius = 10
    self.image = pygame.transform.scale(self.image, (self.radius*2, self.radius*2))
    self.geometry = self.image.get_rect()
    self.geometry.centerx = self.size[0]/2
    self.geometry.centery = self.size[1]*0.8
    self.move_x = cos(angle)
    self.move_y = -sin(angle)
    self.speed = 4

  def draw(self, screen):
    screen.blit(self.image, self.geometry)
    #pygame.draw.rect(screen, (255, 0, 0), self.geometry, 2)
  
  def move(self):
    if 0 >= self.geometry.x:
      self.move_x = -self.move_x
      self.geometry.centerx += 2
    elif self.size[0] <= self.geometry.centerx + self.radius:
      self.move_x = -self.move_x
      self.geometry.centerx -= 2

    if 0 >= self.geometry.y:
      self.move_y = -self.move_y
      self.geometry.y += 2
    elif self.size[1] <= self.geometry.centery + self.radius:
      self.move_y = -self.move_y
      self.geometry.y -= 2
    
    self.geometry.centerx += self.move_x * self.speed
    self.geometry.centery += self.move_y * self.speed

  def collide(self, pf, isbrick = 0):
    x = self.geometry.centerx
    y = self.geometry.centery
    r = self.radius

    if pf.x - r <= x <= pf.x + pf.w + r:
      if pf.y - r <= y <= (pf.y + pf.h + r) + (not isbrick) * self.size[1]:
        if pf.y - r + pf.h*0.3 <= y <= (pf.y + r + pf.h*0.7) + (not isbrick) * self.size[1]:
          self.move_x = -self.move_x
          self.geometry.x += self.move_x
          if isbrick: pf.collides_ball()
        else:
          self.move_y = -self.move_y
          self.geometry.y += self.move_y
          if isbrick: pf.collides_ball()
