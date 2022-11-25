# using with statement
with open('file_path', 'w') as file:
	file.write('hello world !')

  
  # as keyword
  import math as gfg
print(gfg.factorial(5))



# pass keyword
n = 10
for i in range(n):
# pass can be used as placeholder
# when code is to added later
	pass



# Lambda keyword
used to make inline returning functions with no statements allowed internally.
g = lambda x: x*x*x
print(g(7))



# import keyword
import math
print(math.factorial(10))



# from keyword
from math import factorial
print(factorial(10))
