import pygame
from Objects.bonus import Bonus

class Platform():
  def __init__(self, screen, Speed = 4):
    self.size = pygame.display.get_surface().get_size()
    self.w, self.h = 80, 10
    self.x = self.size[0]/2 - self.w/2
    self.y = self.size[1]*0.9
    self.collor = (50, 255, 50)
    self.turns = 0
    self.speed = 2.5
    self.bonuses = {
      'wide_platform': 0
    }
  
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
    pygame.draw.rect(screen, self.collor, (self.x,
    self.y,
    self.w + self.bonuses['wide_platform'] * 10,
    self.h
    ))
  
  def collide_brick(self, brick):
    if pygame.Rect((self.x, self.y), (self.w, self.h)).colliderect(pygame.Rect((brick.x, brick.y), (brick.w, brick.h))):
      self.bonuses[Bonus.bonuses[brick.bonuss.bonus]] += 1
      brick.move_y = 0
      brick.speed = 0
      brick.x = self.size[0] + 50