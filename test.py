rows = 14
collums = 12
name = 'screen'
seat = [
  [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
  [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
  [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
  [1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1],
  [1, 1, 1, 2, 2, 3, 3, 2, 2, 1, 1, 1],
  [1, 1, 1, 2, 2, 3, 3, 2, 2, 1, 1, 1],
  [1, 1, 1, 2, 2, 3, 3, 2, 2, 1, 1, 1],
  [1, 1, 1, 2, 2, 3, 3, 2, 2, 1, 1, 1],
  [1, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1],
  [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
  [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
  [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]]

zaal = '    '
for num in range(1, collums+1):
  if num < 10:
    zaal += '  ' + str(num)
  else: 
    zaal += ' ' + str(num)
zaal += '\n   +'

for line in range(0, collums+1):
  if line < collums:
    zaal += '---'
  else:
    zaal += '--+'
zaal += '\n'

for row in range(rows, 0, -1):
  if row < 10:
    zaal += ' '+ str(row) + ' |'
  else: 
    zaal += str(row) + ' |'
    
  for collum in range(collums):
    if seat[row-1][collum] == 0:
      zaal += '   '
    elif seat[row-1][collum] == 1:
      zaal += '  S' 
    elif seat[row-1][collum] == 2:
      zaal += '  M' 
    elif seat[row-1][collum] == 3:
      zaal += '  V' 
    else:
      zaal += '  X'
  zaal += '  |\n'

zaal += '   +'

for line in range(0, collums+1):
  if line < collums:
    zaal += '---'
  else:
    zaal += '--+'
zaal += '\n     '

for text in range(collums*3):
  zaal += '-'
zaal += '\n     '

for text in range(collums*3+1 - len(name)):
  if text == collums * 3 // 2 - len(name) // 2:
    zaal += name
  else:
    zaal += ' '

print(zaal)