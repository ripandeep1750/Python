Iteration Keywords – for, while, break, continue

# Using for loop
for i in range(10):

	print(i, end = " ")
	
	# break the loop as soon it sees 6
	if i == 6:
		break
	
print()
	
  
  
  
  
# loop from 1 to 10
i = 0
while i <10:
	
	# If i is equals to 6,
	# continue to next iteration
	# without printing
	if i == 6:
		i+= 1
		continue
	else:
		# otherwise print the value
		# of i
		print(i, end = " ")
		
	i += 1

  
  
  
  
  Conditional keywords – if, else, elif
i = 20
if (i == 10):
	print ("i is 10")
elif (i == 20):
	print ("i is 20")
else:
	print ("i is not present")

  
  
  
 # def keyword
def fun():
	print("Inside Function")
	
fun()




# Return keyword
def fun():
	S = 0
	
	for i in range(10):
		S += i
	return S

print(fun())




# Yield Keyword
def fun():
	S = 0
	
	for i in range(10):
		S += i
		yield S

for i in fun():
	print(i)

  
