#### BA 1
money = 1000

if  money >= 1000000:
  millionaire = True
else:
  millionaire = False

answer = 'That is most definitely ' + str(millionaire)

print(answer)

#### BA 2
isDog = True
isBrown = True

if (isDog and isBrown):
  decision = 'adopt this pet'
else:
  decision = 'search for another pet'

print(decision)

#### BA 3
niceWeather = True
appointment = True

if (niceWeather or appointment):
  decision = 'go out'
else:
  decision = 'stay home'

print(decision)

#### BA 4
x = 55
y = 60

if x > y:
  s = 'Max is x.'
if y > x:
  s = 'Max is y.'
elif x == y:
  s = 'Numbers are equal.'

print(s)

#### BA 5
n = 5

if (n > 0):
  n
else:
  n = n + -n * 2

print(n)

#### BA 6
x = 7
y = 8
z = 5

minimum = min(x, y, z)

if (x == minimum) :
  minStr = 'min is x : ' + str(minimum)
elif (y == minimum) :
  minStr = 'min is y : ' + str(minimum)
else :
  minStr = 'min is z : ' + str(minimum)

print(minStr)

#### BA 7
grade = 4.3
threshold = 5.5

if (grade < threshold) :
  result = 'fail'
else :
  result = 'pass'

print(result)

#### BA 8
number = 5

if (0 < number) :
  s = 'the number is positive'
elif (0 == number) :
  s = 'the number is 0'
else :
  s = 'the number is negative'

print(s)

#### BA 9
number = 10

if (0 < number) :
  if (number % 2) == 0 : 
    status = str(number) + ' is even and positive'
  else : 
    status = str(number) + ' is odd and positive'
elif (0 == number) : 
  status = str(number) + ' is even'
else :
  if (number % 2) == 0: 
    status = str(number) + ' is even and negative'
  else : 
    status = str(number) + ' is odd and negative'

print(status)

#### BA 10
year = 2019

if ((year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0)) :
  isLeap = True
else:
  isLeap = False

print(isLeap)

#### BA 11
points = 35
totalPoints = 50

percentage = points / totalPoints * 100

if (percentage < 50) :
  remarks = 'Unsatisfactory'
elif (percentage < 70) :
  remarks = 'Satisfactory'
elif (percentage < 90) :
  remarks = 'Good'
else :
  remarks = 'Excellent'

print(remarks)

#### BA 12
paymentMethod = 'Cash on delivery' # iDeal, Credit Card, Other Payment
deliveryMethod = 'Pickup' # Home Delivery
billAmount = 700
thresholdAmount = 500

if (paymentMethod == 'Cash on delivery') :
  billAmount += 5

elif (paymentMethod == 'Credit Card') :
  if (billAmount < thresholdAmount) :
    billAmount += 3

elif (paymentMethod != 'iDeal') :
  billAmount += 10
  
if (deliveryMethod == 'Home Delivery') and (billAmount < thresholdAmount) :
    billAmount += 5

print(billAmount)

#### BA 13
n = 45

if (n % 3) == 0 and (n % 5) == 0 :
  output = 'Purple'
elif (n % 3) == 0 :
  output = 'Blue'
elif (n % 5) == 0 :
  output = 'Red'
else :
  output = 'Razzmatazz'

print(output)

#### BA 14
number = 8
divisor = 4

if (number % divisor) == 0 :
  output = str(number) + ' is divisible by ' + str(divisor)
else :
  output = str(number) + ' is NOT divisible by ' + str(divisor)

print(output)

#### BA 15
day = 1

days = ['ERROR: day of the week unknown', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'ERROR: day of the week unknown']
s = str(days[day])

print(s)

#### BA 16
diceone = 1
dicetwo = 2

dices = diceone + dicetwo

if (dices % 2) == 1 :
  dishes = 'Mom'
else :
  if (dices % 4) == 0 and (diceone == dicetwo) :
    dishes = 'Dad'
  elif (dices % 4) == 0:
    dishes = 'Joe'
  else :
    dishes = 'Sue'

print(dishes)

#### BA 17
n = 979

num = str(n)
if(num == num[::-1]) :
  output = num + ' is a palindrome'
else:
  output = num + ' is NOT a palindrome'

print(output)

#### BA 18
day = 21
month = 3

cal = month * 100 + day 

if (cal >= 321 and cal <= 620) :
  season = 'Spring'
elif (cal >= 621 and cal <= 920) :
  season = 'Summer'
elif (cal >= 921 and cal < 1220) :
  season = 'Autumn'
else :
  season = 'Winter'

print(season, cal)