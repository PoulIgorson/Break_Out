import pygame
import sys
from Objects.ball import Ball
from Objects.platform_ import Platform
from Objects.brick import Brick
from Game_over import Game_over

def generate_bricks(screen):
  bricks = []
  for i in range(5):
    for j in range(10):
      bricks.append(Brick(screen, i, j))
  return bricks

def break_out():
  fps = 33
  size = width, height = 500, 350
  pygame.init()
  pygame.display.set_caption('BreakOut')
  screen = pygame.display.set_mode(size, pygame.RESIZABLE)

  font = pygame.font.SysFont('Comic Sans MS', int(55*width/500), True)

  BLACK = (0, 0, 0)

  ball = Ball(screen)
  pf = Platform(screen, ball.speed)
  bricks = generate_bricks(screen)

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
    ball.move(pf.bonuses['god_mode'])
    pf.moves()
    pf.update_bonus()
    for i in range(len(bricks)):
      ball.collide(bricks[i], 1)
      if pf.collide_brick(bricks[i], fps) == 'del':
        bricks[i] = 0
      if bricks[i] != 0: bricks[i].moves()
    i = 0
    while 0 in bricks:
      if bricks[i] == 0:
        del bricks[i]
        i -= 1
      i += 1

    score = font.render(f'{Brick.score}', True, (200, 100, 150))
    print(pf.bonuses['wide_platform'])
    print(pf.bonuses['god_mode'], '\n')

    # отрисовка
    screen.fill(BLACK)
    ball.draw(screen, pf.bonuses['god_mode'], fps)
    pf.draw(screen)
    for i in range(len(bricks)):
      bricks[i].draw(screen)
    screen.blit(score, (20, 30))
    if (not pf.bonuses['god_mode']) and Game_over(ball.geometry.centery, pf.y, width, height, screen, fps, Brick.score): game_over = True

    pygame.display.flip()

    # подождать
    pygame.time.wait(int(1000/fps))
    
  sys.exit()


if __name__ == '__main__':
  break_out()
