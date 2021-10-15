import pygame
import sys
from ball import Ball
from platform_ import Platform
from brick import Brick
from Game_over import Game_over

fps = 30

def break_out():
  size = width, height = 500, 350
  pygame.init()
  pygame.display.set_caption('BreakOut')
  screen = pygame.display.set_mode(size, pygame.RESIZABLE)

  font = pygame.font.SysFont('Comic Sans MS', int(55*width/500), True)

  BLACK = 0, 0, 0

  ball = Ball(screen)
  pf = Platform(screen)
  bricks = [Brick(screen, i) for i in range(20)]

  god_mode = 0
  gm_time = 15 * int(1000/fps)

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
    for brick in bricks:
      ball.collide(brick, 1)

    if god_mode: gm_time -= 1
    if gm_time == 0:
      god_mode = not god_mode
      gm_time = 15 * int(1000/fps)
    

    score = font.render(f'{Brick.score}', True, (200, 100, 150))

    # отрисовка
    screen.fill(BLACK)
    ball.draw(screen)
    pf.draw(screen)
    for brick in bricks:
      brick.draw(screen)
    screen.blit(score, (20, 30))
    if (not god_mode) and Game_over(ball.geometry.centery, pf.y, width, height, screen, fps): game_over = True

    pygame.display.flip()

    # подождать
    pygame.time.wait(int(1000/fps))
    
  sys.exit()


if __name__ == '__main__':
  break_out()
