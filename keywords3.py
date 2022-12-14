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



Exception Handling Keywords – try, except, raise, finally, and assert
a = 4
b = 0
# No exception Exception raised in try block
try:
	k = a//b # raises divide by zero exception.
	print(k)

# handles zerodivision exception
except ZeroDivisionError:
	print("Can't divide by zero")

finally:
	# this block is always executed
	# regardless of exception generation.
	print('This is always executed')

# assert Keyword
# using assert to check for 0
print ("The value of a / b is : ")
assert b != 0, "Divide by 0 error"
print (a / b)



#del Keyword
my_variable1 = 20
my_variable2 = "GeeksForGeeks"

# check if my_variable1 and my_variable2 exists
print(my_variable1)
print(my_variable2)

# delete both the variables
del my_variable1
del my_variable2

# check if my_variable1 and my_variable2 exists
print(my_variable1)
print(my_variable2)



 #Global and nonlocal keywords
	# global variable
a = 15
b = 10

# function to perform addition
def add():
	c = a + b
	print(c)

# calling a function
add()

# nonlocal keyword
def fun():
	var1 = 10

	def gun():
		# tell python explicitly that it
		# has to access var1 initialized
		# in fun on line 2
		# using the keyword nonlocal
		nonlocal var1
		
		var1 = var1 + 10
		print(var1)

	gun()
fun()
