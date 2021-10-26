#### BA 1
x = 3
y = 3.5
z = x * 3
k = y + 9 + 5.0
w = int(k)
t = 2
j = z - 3 - t
h = z - 2.5 - t

print(x, y, z, k, w, t, j, h)

#### BA 2
x =  True
y =  False

a = x  and  y
b = x  or  y
c = not y
d = y and b and c
e = 5 >= x

print(c)

#### BA 3
salutation = 'Hi'
name1 = 'John'
name2 = 'Jessica'

greet1 = salutation + ' ' + name1 + '!'
greet2 = salutation + ' ' + name2 + '!!!'
years = 35

howOld = name1 + ' is ' + str(years) + ' years old'
length = len(howOld)

print(length)

#### BA 4
a = 5
b = 3
c = 'Hello'
d = 5

ans1 = a == 4.6
ans2 = b == a - 2
ans3 = c == c
ans4 = d == a

result = 'The first is ' + str(ans1) \
       + ', the second is ' + str(ans2) \
       + ', the third is ' + str(ans3) \
       + ', the fourth is ' + str(ans4)

print(result)

#### BA 5
eggs = 27

eggsLeft = eggs % 12
dozens = int(eggs / 12)

print(dozens)

### BA 6
eggs = 1342

eggsLeft = eggs % 144   
finalEggsLeft = eggs % 12
howManyGross = int(eggs / 144)
howManyDozensInEggsLeft = int(eggsLeft / 12)

print(eggsLeft, finalEggsLeft, howManyDozensInEggsLeft, howManyGross)

#### BA 7
totalSeconds = 98765

minutes, seconds = divmod(totalSeconds, 60)
hours, minutes = divmod(minutes, 60)

time = "%d:%02d:%d" % (hours, minutes, seconds)

print(time)

#### BA 8
n = 485

hundreds = int(repr(n)[-3])
tens = int(repr(n)[-2])
units = int(repr(n)[-1])

print(hundreds, tens, units)

#### BA 9
n = 9385

thousands = int(repr(n)[-4])
hundreds = int(repr(n)[-3])
tens = int(repr(n)[-2])
units = int(repr(n)[-1])

print(thousands, hundreds, tens, units)