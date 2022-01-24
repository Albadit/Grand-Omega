###### Test 1
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

###### Practice 1
#### BA 1
name = 'Programming basics'
questionsCorrection = 'TFFTFTTTFTFF'
theoryGrade = '14.5'
practiceGrade = '8.5'

total_point = str(len(questionsCorrection))
finalGrade = round((float(theoryGrade) + float(practiceGrade)) / 2) - 1

if finalGrade >= 11:
  passedCourse = True
else:
  passedCourse = False

explanation = 'The ' + name + ' exams have ' + total_point + ' questions'

print(explanation)

#### BA 2
daysLiving = 760

years = daysLiving // 360
yearss = daysLiving % 360
months = yearss // 30
days = yearss % 30

if years == 1: name_years = ' year\n'
else: name_years = ' years\n'

if months == 1: name_months = ' month\n'
else: name_months = ' months\n'

if days == 1: name_days = ' day\n'
else: name_days = ' days\n'

age = str(years) + name_years + str(months) + name_months + str(days) + name_days

print(age)

#### BA 3
n = 97634
alternating = True

n_string = str(n)
n_map = map(int, n_string)
n_list = list(n_map)

if n_list[0] % 2 == 0: 
  even_list = n_list[::2]
  uneven_list = n_list[1::2]
else:
  even_list = n_list[1::2]
  uneven_list = n_list[::2]

for i in range(len(even_list)):
  if even_list[i] % 2 == 0: 
    continue
  else:
    alternating = False
    break

for j in range(len(uneven_list)):
  if not uneven_list[j] % 2 == 0: 
    continue
  else:
    alternating = False
    break

print(alternating)

#### BA 4
nRows = 5
counter = 1
triangle = '*\n'

while counter <= nRows:
  for i in range(1, counter+1):
    if counter*i < 10: add = '0'
    else: add = ''
    triangle = triangle + '(' + add + str(counter*i) + ')'
  triangle = triangle + '\n'
  counter += 1

print(triangle)

#### BA 5 
width = 2
height = 8
size = 6

counter = size
counters = height
s = ''
lag = height - size

while not counters < 1:

  for j in range(width):
    s = s + '|'

  for i in range(counter):
    s = s + '*'
  s = s + '\n'

  if counters == 0:
    for k in range(lag):
      for l in range(width):
        s = s + '|'
  counter -= 1
  counters -= 1

print(s)