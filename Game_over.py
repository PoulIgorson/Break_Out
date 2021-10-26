from sys import exit
import pygame
from Highscores import save, load

def input_name(screen, width, height, fps, scores):
  input_word = 0
  name = ''
  font = pygame.font.SysFont('Comic Sans MS', int(30*width/500), True)
  score = scores
  while not input_word:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        exit()
      
      if event.type == pygame.KEYDOWN and not input_word:
        if event.key == pygame.K_q: name += 'q'
        if event.key == pygame.K_w: name += 'w'
        if event.key == pygame.K_e: name += 'e'
        if event.key == pygame.K_r: name += 'r'
        if event.key == pygame.K_t: name += 't'
        if event.key == pygame.K_y: name += 'y'
        if event.key == pygame.K_u: name += 'u'
        if event.key == pygame.K_i: name += 'i'
        if event.key == pygame.K_o: name += 'o'
        if event.key == pygame.K_p: name += 'p'
        if event.key == pygame.K_a: name += 'a'
        if event.key == pygame.K_s: name += 's'
        if event.key == pygame.K_d: name += 'd'
        if event.key == pygame.K_f: name += 'f'
        if event.key == pygame.K_g: name += 'g'
        if event.key == pygame.K_h: name += 'h'
        if event.key == pygame.K_j: name += 'j'
        if event.key == pygame.K_k: name += 'k'
        if event.key == pygame.K_l: name += 'l'
        if event.key == pygame.K_z: name += 'z'
        if event.key == pygame.K_x: name += 'x'
        if event.key == pygame.K_c: name += 'c'
        if event.key == pygame.K_v: name += 'v'
        if event.key == pygame.K_b: name += 'b'
        if event.key == pygame.K_n: name += 'n'
        if event.key == pygame.K_m: name += 'm'
        if event.key == pygame.K_SPACE: name += '_'
        if event.key == 13: input_word = 1
    
    screen.fill((0, 0, 0))
    over = font.render(f'GAME OWER', True, (255, 200, 200))
    scores = font.render(f'Your scores: {score}', True, (200, 230, 210))
    text = font.render(f'Your name: {name}', True, (200, 230, 210))
    text_size = text.get_size()
    score_size = scores.get_size()
    over_size = over.get_size()
    screen.blit(over, (width/2-over_size[0]/2, height/2-over_size[1]-score_size[1]-text_size[1]/2))
    screen.blit(scores, (width/2-score_size[0]/2, height/2-score_size[1]-text_size[1]/2))
    screen.blit(text, (width/2-text_size[0]/2, height/2-text_size[1]/2))
    pygame.display.flip()
    pygame.time.wait(int(1000/fps))
  return name

def Game_over(pos_ball, pos_platform, width, height, screen, fps, score):
  if pos_ball > pos_platform:
    table = load()
    table.append([input_name(screen, width, height, fps, score), score])
    save(table)
    t = 0
    font = pygame.font.SysFont('Comic Sans MS', int(30*width/500), True)
    while t < 5*fps:
      screen.fill((0, 0, 0))
      y = 10
      for text in table:
        text[1] = str(text[1])
        text_ = font.render(' '.join(text), True, (255, 255, 255))
        screen.blit(text_, (10, y))
        y += 30*width/500

      pygame.display.flip()
      t += 1
      pygame.time.wait(int(1000/fps))
    return 1