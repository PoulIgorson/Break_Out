from platform_ import Platform

class Brick(Platform):
  score = 0
  def __init__(self, screen, iters, jters):
    super().__init__(screen)
    self.collor = (240, 200, 250)
    self.speed = 0
    self.w, self.h = int(self.size[0]/10), int(self.size[1] * 0.05)
    self.x = 2 + (int(self.size[0]/10) + 1) * jters
    self.y = 2 + int(self.size[1]/10) * iters - iters*(int(self.size[1]/10)/2 - 1)
  
  def collides_ball(self):
    self.x = self.size[0] + 50
    self.y = self.size[1] + 50
    Brick.score += 1