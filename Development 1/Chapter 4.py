#### BA 1
x = 10
while x > 0 :
  x = x - 1

print(x)

#### BA 2
x = 19
limit = 7
while x > limit :
  x = x - 2
print(x)

#### BA 3
x = -4
step = 1

while x < 6 :
  x += step

print(x)

#### BA 4
start = 0
end = 5
incr = 1

i = start

while i < end  :
  i += incr

print(i)

#### BA 5
x = 5.9
limit = 5.1
step = -0.2

while x > limit:
  x += step

#### BA 6
y = 0
maximum = 5

while y < maximum:
  y = y + 1
z = 0
while z <= maximum:
  z = z + 1
  
print(z, y)

#### BA 7
howManyInBed = 10
song = ''

while 1 < howManyInBed  :
  song += str(howManyInBed) + ' in a bed and the little one said,\n'
  song += '``Roll over, roll over``\n'
  song += 'They all rolled over and one fell out,\n'
  howManyInBed -= 1

song += str(howManyInBed) + ' in a bed and the little one said,\n'  
song += '``Alone at last``'

print(song)

#### BA 8
n = 1

while n <= 10:
  n += 1
  form = n - 1
  squared = form * form
  res = str(n - 1) + ' squared is ' + str(squared)

print(res)

#### BA 9
n = 5

while n <= 100:
  squared = n * n
  res = str(n) + ' squared is ' + str(squared)
  n += 5

print(n, res, squared)

#### BA 10
n = 10

while  n > 0: 
  squared = int(n / 2)
  res = str(n) + ' halved is ' + str(squared)
  n -= 2

print(n, res, squared)

#### BA 11
x = 1
divisibleBy = ''

while (x < 11) :
  if (x % 2) == 0 :
    divisibleBy = str(x) + ' is divisible by 2'
  if (x % 3) == 0 :
    divisibleBy = str(x) + ' is divisible by 3'
  if (x % 4) == 0 :
    divisibleBy = str(x) + ' is divisible by 4'
  if (x % 5) == 0 :
    divisibleBy = str(x) + ' is divisible by 5'
  x = x + 1

print(x, divisibleBy)

### BA 12 Don't know


#### BA 13
isItDay = False
isItNight = not isItDay

hour = 0
while hour < 24:  
  if hour <= 5  :
    isItDay = False
  elif hour <= 17:
    isItDay = True
  else:
    isItDay = False
  isItNight = not isItDay
  hour = hour + 1

print(isItDay, isItNight)

#### BA 14
start = 1
end = 4
s = ''
print()

while start <= end:
  
  start1 = str(start)
  s += start1
  start += 1


print(s, start)

#### BA 15 t/m 31