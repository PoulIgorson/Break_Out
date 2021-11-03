import pygame
from random import randint as rand

class Bonus:
  count_bonus = 0
  bonuses = []
  def __init__(self, screen, pf):
    self.size = pygame.display.get_surface().get_size()
    if len(Bonus.bonuses) == 0:
      with open('bonus.txt', 'r') as f:
        for name in f.readlines():
          Bonus.bonuses.append(name.strip())
          Bonus.count_bonus += 1
        
    self.bonus = rand(1, Bonus.count_bonus)
  
  def wide_platform(pf):
    pf.bonuses['wide_platform'] += 1
  
  def god_mode(pf, fps=30):
    pf.bonuses['god_mode'] = 10 * fps
