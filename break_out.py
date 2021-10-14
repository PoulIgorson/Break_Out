import pygame
import sys
from ball import Ball
from platform_ import Platform

fps = 30

def break_out():
  size = width, height = 500, 350
  pygame.init()
  pygame.display.set_caption('BreakOut')
  screen = pygame.display.set_mode(size, pygame.RESIZABLE)

  BLACK = 0, 0, 0

  ball = Ball(screen)
  pf = Platform(screen)

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
    ball.move()
    pf.moves()

    # отрисовка
    screen.fill(BLACK)
    ball.draw(screen)
    pf.draw(screen)

    pygame.display.flip()

    # подождать
    pygame.time.wait(fps)
    
  sys.exit()


if __name__ == '__main__':
  break_out()
