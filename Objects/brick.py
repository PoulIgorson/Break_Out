from Objects.platform_ import Platform
from Objects.bonus import Bonus

class Brick(Platform):
  score = 0
  def __init__(self, screen, iters, jters):
    super().__init__(screen)
    self.collor = (240, 200, 250)
    self.speed = 0
    self.w, self.h = int(self.size[0]/10), int(self.size[1] * 0.05)
    self.x = 2 + (int(self.size[0]/10) + 1) * jters
    self.y = 2 + int(self.size[1]/10) * iters - iters*(int(self.size[1]/10)/2 - 1)
    self.move_y = 0
    self.bonuss = Bonus(screen, self)
  
  def moves(self):
    self.y += self.speed * self.move_y
  
  def collides_ball(self):
    Brick.score += 1
    self.move_y = 1
    self.move_x = 0
    self.speed = 2