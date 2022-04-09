###### Test 2
#### BA 1
# def reverse(n):
#   rev = str(n)[::-1]
#   rev = int(rev)
#   return rev

# def isPalindrome(n):
#   if n == reverse(n):
#     return True
#   else:
#     return False

# n = 123
# a = reverse(n)
# b = isPalindrome(n)
# print(a,b)

# #### BA 2
# def sumUpTo(n):
#   global point
#   point += n 
#   n -= 1
#   if n > 0:
#     sumUpTo(n)
#   elif n <= 0: 
#     return 0
#   return point

# point = 0
# a = 5
# result = sumUpTo(a)

# print(result)

# L = [i for i in range(10,30,10)] * 2
# print(L)

# def repeat(n, sym):
#   text = ''
#   for i in range(n):
#     text += sym
#   return text

# def line(n):
#   sym = '*'
#   return repeat(n, sym)

# def square(n):
#   return repeat(n, line(n) + '\n')

# def rectangle(width, height):
#   return repeat(height , line(width) +  '\n')

# s = square(5) 
# r = rectangle(5, 3)

# print(r)

def count(a, b):
  print()
  if a >= b:
    if a == b:
      return  a
    return ''
  else:
    partial = count(a + 1, b - 1)
    return str(a) + str(partial) + str(b)

a = 0
b = 10
s = count(a, b)
print(s)