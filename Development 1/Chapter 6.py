### BA 1 t/m 11

#### BA 11
height = 4
s = ''

for i in range(0, height):
  for j in range(0, i):
    s = s + '-'
  s = s + '*'
  for j in range(0, i//2):
    s = s + '-'
  s = s + '\n'
  
print(s)

#### BA 12 Don't work
size = 5
s = ''
# w = 0

# while (w < size):
#   s = s + '+'
#   w += 1
# s = s + '\n'

for i in range(0, size):
  s = s + '+'
s = s + '\n'

for i in range(0, size-2):
  s = s + '+'
  for j in range(0, i+1):
    s = s + '='
  for k in range(i, size-3,):
    s = s + '#'
  s = s + '+'
  s = s + '\n'

for i in range(0, size):
  s = s + '+'
s = s + '\n'

print(s)

#### BA 13
side = 5
s = ''

for i in range(0, side):
  s = s + '*'
s = s + '\n'

for i in range(0, side-2):
  s = s + '*'
  for j in  range(0, side-2):
    s = s + ' '
  s = s + '*'
  s = s + '\n'

for i in range(0, side):
  s = s + '*'
s = s + '\n'

print(s)

#### 14
l = 4
s = ''

for i in range(0, l//2):
  for j in range(0, l//2):
    s = s + '*'
  for k in range(0, l//2):
    s = s + '+'
  s = s + '\n'

for i in range(0, l//2):
  for j in range(0, l//2):
    s = s + '-'
  for k in range(0, l//2):
    s = s + '='
  s = s + '\n'

print(s)

#### BA 15
h = 5
s = ''

for i in range(0, h//2+1):
  for j in range(0, i+1):
    s = s + '*'
  s = s + '\n'

for i in range(h//2+1, 1, -1):
  for j in range(0, i-1):
    s = s + '*'
  s = s + '\n'

print(s)

### BA 16
w = 5
h = 6
s = ''
for i in range(0, w):
  s = s + '='
s = s + '\n'
for j in range(0, h-2):
  s = s + '|'
  for k in range(0, w-2):
    s = s + '*'
  s = s + '|'
  s = s + '\n'
for n in range(0, w):
  s = s + '='
s = s + '\n'
# print(s)

#### BA 17
size = 5

timestable = '  |'
for i in range(1, size+1):
  timestable = timestable + '  ' + str(i)
timestable = timestable + '\n'

timestable = timestable + '--+---------------\n'

for j in range(1, size+1):
  timestable = timestable + str(j) + ' |'
  for l in range(1, size+1):
    if (l*j < 10):
      timestable = timestable + '  ' + str(l*j)
    else:
      timestable = timestable + ' ' + str(l*j)
    times = l*j 
  timestable = timestable + '\n'

print(timestable)