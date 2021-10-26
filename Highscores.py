def load(name='highscores.txt'):
  table = []
  with open(name, 'r') as f:
    for t in f.readlines():
      t = t.strip().split()
      table.append([t[0], int(t[1])])
  return table

def save(table, name='highscores.txt'):
  with open(name, 'w') as f:
    for i in range(len(table)):
      f.write(' '.join([str(x) for x in table[i]])+'\n')