import pygame
from random import randint as rand

class Bonus:
  count_bonus = 0
  bonuses = []
  def __init__(self, screen, pf):
    self.size = pygame.display.get_surface().get_size()
    with open('bonus.txt', 'r') as f:
      for name in f.readlines():
        Bonus.bonuses.append(name)
        Bonus.count_bonus += 1

    self.bonus = rand(1, Bonus.count_bonus)
  
  def wide(self, pf):
    try:
      pf.bonuses['wide_platform'] += 1
    except:
      pf.bonuses['wide_platform'] = 0