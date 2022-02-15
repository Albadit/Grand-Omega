# x = (True and not True) or (False and False)
# y = True and (False or True or not False)

# print(x, y)

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

# def reverse(n):
#   print()
#   global rev
#   rev = 0
#   while(n > 0):
#     a = n % 10
#     rev = rev * 10 + a
#     n = n // 10
#   return rev

# def isPalindrome(n):
#   if rev % 2 == 0:
#     return True
#   else:
#     return False

# n = 4554
# a = reverse(n)
# b = isPalindrome(n)
# print(a,b)

L = [i for i in range(10,30,10)] * 2
print(L)