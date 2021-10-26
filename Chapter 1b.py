#### BA 1
a = 2 + 2 + 2
b = 3 * (3 + 3)
c = 5 + 4 * 3 / (4 + -2 + 1) 
d = 5 * 4 / (3 + 2) - 1

print(a, b, c, d)

#### BA 2
x = 1
y = x + 3
z = y
w = z * (-2)
x = z / 8

print(z, y, x, w)

#### BA 3
a = 4 + 2
b = a - 3
c = a * b
d = c - 13.5

print(a, b, c, d)

#### BA 4
a, b = 5, 3

c = a * b + 1
a = 0
b = 0

print(c)

#### BA 5
a, b, c = 20, 0, 0

res = a - b * c
a = 0
b = 0
c = 0

print(res)

#### BA 6
meters = 2
centimeters = meters * 100

print(centimeters)

#### BA 7
appleQuantity = 9
applePrice = 3
bananaQuantity = 15
bananaPrice = 2
cherryQuantity = 3
cherryPrice = 10
persons = 3

costPerPerson = ((appleQuantity * applePrice) + (bananaQuantity * bananaPrice) + (cherryQuantity * cherryPrice)) / persons

print(costPerPerson)

#### BA 8
milk = 4
milkPrice = 1
bread = 2
breadPrice = 2
butter = 1
butterPrice = 3
egg = 3 
eggPrice = 3
tax = 15

totalCost = ((milk * milkPrice) + (bread * breadPrice) + (butter * butterPrice) + (egg * eggPrice)) / 100 * (100 + tax)

print(totalCost)

#### BA 9
wWidth = 8
wHeight = 3
wThickness = 2
costPerCubicMeter = 250
dWidth = 1
dHeight = 2
doorPrice = 500

wArea = wWidth * wHeight
dArea = dWidth * dHeight
concreteRequired = (wArea - dArea) * wThickness
totalCost = costPerCubicMeter * concreteRequired + doorPrice

print(totalCost)

#### BA 10
houseValue = 300000
carValue = 10000
overdueInstallments = 10
installment = 1000
kids = 2
siblings = 4

assetsValue = houseValue + carValue - installment * overdueInstallments
kidShare = assetsValue / 3 * 2 / kids
siblingShare = assetsValue / 3 / siblings

print(assetsValue)

#### BA 11
radius = 3
pi = 3
boxSide = radius * 2 + 1
vGlobe = 4 / 3 * pi * radius ** 3
vBox = boxSide ** 3
vEmpty = vBox - vGlobe

print(vEmpty)

#### BA 12
sideCubeOne = 2
sideCubeTwo = 3
sideBox = 5

a = sideCubeOne ** 3
b = sideCubeTwo ** 3
c = sideBox ** 3 
vEmpty = sideBox ** 3 - sideCubeOne ** 3 - sideCubeTwo ** 3

print(vEmpty)

#### BA 13
a = 'hello'
b = 'world'

a, b = b, a

print(a, b)