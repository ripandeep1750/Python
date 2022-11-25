# Python code to demonstrate working of iskeyword()
import keyword
print("The list of keywords is : ")
print(keyword.kwlist)


print(False == 0)
print(True == 1)

print(True + True + True)
print(True + False + False)

print(None == 0)
print(None == [])


# showing logical operation
# or (returns True)
print(True or False)

# showing logical operation
# and (returns False)
print(False and True)

# showing logical operation
# not (returns False)
print(not True)

# using "in" to check
if 's' in 'geeksforgeeks':
	print("s is part of geeksforgeeks")
else:
	print("s is not part of geeksforgeeks")

# using "in" to loop through
for i in 'geeksforgeeks':
	print(i, end=" ")

print("\r")

# using is to check object identity
# string is immutable( cannot be changed once allocated)
# hence occupy same memory location
print(' ' is ' ')

# using is to check object identity
# dictionary is mutable( can be changed once allocated)
# hence occupy different memory location
print({} is {})
