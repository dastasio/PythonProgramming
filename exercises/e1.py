def factorial( n):
	if n == 0:
		return 1
	else:
		return n * factorial( n - 1)


num = int( input( "Give me a number: "))
print ("\nThe Factorial is: " + str( factorial(num)))
