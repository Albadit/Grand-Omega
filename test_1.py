#### B1
timelapse = 234866

days = timelapse // (24 * 3600)
times = timelapse % (24 * 3600)
hours = times // 3600
times %= 3600
minutes = times // 60

time = str(days) + ' days\n' + str(hours) + ' hours\n' + str(minutes) + ' minutes'
print(time)

#### B2
courseName = 'Alba'
courseCode = 'alba123'

grade1, grade2 = 4.5, 6.5

gradeAverage = (grade1 + grade2) / 2
gradeReported = round((grade1 + grade2) / 2)

if gradeAverage >= 5.5:
  passed = True
  pas = 'passed ' + courseCode
else:
  passed = False
  pas = 'failed ' + courseName

result = 'Student has scored ' + str(gradeReported) + ' and has ' + pas

print(result)

#### BA 3
n = 12
if n % 2 == 0:
  isWellDivisible = True
elif n == 7:
  isWellDivisible = True
else:
  isWellDivisible = False
  
print(isWellDivisible)

#### BA 4
height = 5
s = ''

for i in range(0, height):
  for k in range(i, height-1):
    s = s + '*'
  s = s + '/'
  for j in range(0, i):
    s = s + '*'
  s = s + '\n'

print(s)

#### BA 5
l = 9
s = ''

for i in range(0, l//2):
  for j in range(0, l//2):
    s = s + '*'
  if l % 2 == 0:
    for k in range(0, l//2):
      s = s + '+'
  else:
    for k in range(0, l//2+1):
      s = s + '+'
  s = s + '\n'

for i in range(0, l//2):
  for j in range(0, l//2):
    s = s + '-'
  if l % 2 == 0:
    for k in range(0, l//2):
      s = s + '='
  else:
    for k in range(0, l//2+1):
      s = s + '='
  s = s + '\n'

print(s)