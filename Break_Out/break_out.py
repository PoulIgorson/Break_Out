import pygame
import sys
from Break_Out.Objects.ball import Ball
from Break_Out.Objects.platform_ import Platform
from Break_Out.Objects.brick import Brick
from Break_Out.Game_over import Game_over
from Break_Out.Objects.bonus import Bonus

def generate_bricks(screen):
  bricks = []
  for i in range(5):
    for j in range(10):
      bricks.append(Brick(screen, i, j))
  return bricks

def break_out():
  fps = 30
  size = width, height = 500, 350
  pygame.init()
  pygame.display.set_caption('BreakOut')
  screen = pygame.display.set_mode(size, pygame.RESIZABLE)

  font = pygame.font.SysFont('Comic Sans MS', int(55*width/500), True)

  BLACK = (0, 0, 0)

  ball = Ball(screen)
  pf = Platform(screen, ball.speed)
  bricks = generate_bricks(screen)

  line_draw = []

  god_mode = 1
  gm_time = 500 * int(1000/fps) * 1000000

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
        
        if pygame.K_g == event.key:
          god_mode = not god_mode
      
      if event.type == pygame.KEYUP:
        if pygame.K_a == event.key or pygame.K_d == event.key:
          pf.turn(0)
    
    # логика работы игры
    ball.collide(pf)
    ball.move()
    pf.moves()
    for i in range(len(bricks)):
      ball.collide(bricks[i], 1)
      pf.collide_brick(bricks[i])
      bricks[i].moves()

    if god_mode: gm_time -= 1
    if gm_time == 0:
      god_mode = not god_mode
      gm_time = 15 * int(1000/fps)

    score = font.render(f'{Brick.score}', True, (200, 100, 150))

    # отрисовка
    screen.fill(BLACK)
    ball.draw(screen)
    pf.draw(screen)
    for i in range(len(bricks)):
      bricks[i].draw(screen)
    screen.blit(score, (20, 30))
    if (not god_mode) and Game_over(ball.geometry.centery, pf.y, width, height, screen, fps, Brick.score): game_over = True

    pygame.display.flip()

    # подождать
    pygame.time.wait(int(1000/fps))
    
  sys.exit()


if __name__ == '__main__':
  break_out()
