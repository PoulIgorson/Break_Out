import pygame

def Game_over(pos_ball, pos_platform, width, height, screen, fps):
  if pos_ball > pos_platform:
    t = 0
    text = 'GAME OVER'
    font = pygame.font.SysFont('Comic Sans MS', int(55*width/500), True)
    text = font.render(f'{text}', True, (255, 100, 20))
    text_size = text.get_size()
    while t < 2000 / fps:
      screen.fill((0, 0, 0))
      screen.blit(text, (width/2-text_size[0]/2, height/2-text_size[1]/2))
      pygame.display.flip()
      t += 1
      pygame.time.wait(int(1000/fps))
    return 1