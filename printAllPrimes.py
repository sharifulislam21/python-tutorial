## Prime Numbers

lower = 100
upper = 4000

print("Prime Numbers:")

for num in range(lower, upper+1):
	if num > 1 :
		for i in range(2, num):
			if (num%i==0):
				break
			else:
				print(num)