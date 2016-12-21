def add( x, y):
	return x + y

def sub( x, y):
	return x - y

def mult( x, y):
	return x * y

def div( x, y):
	return x / y

def power( n, p):
	temp_result = n
	i = 1
	while( i < p):
		temp_result *= n
		i += 1
	return temp_result

def printMenu():
	print ( "Welcome to the Calculator!")
	print ( "MENU:")
	print ( "1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Power\n")
	choice = getNum( "Please choose an option: ")
	return choice

def getNum( string = ' '):
	return int(input( string))

if __name__ == "__main__":
	op = printMenu()

	if 0 < op > 5:
		print ( "\nERROR: " + str(op) + " is not a valid option!\n\nEXITING...")
		input()
	else:
		a = getNum( "Enter first number: ")
		b = getNum( "Enter second number: ")
		if op == 1:
			result = add( a, b)
		elif op == 2:
			result = sub( a, b)
		elif op == 3:
			result = mult( a, b)
		elif op == 4:
			result = div( a, b)
		elif op == 5:
			result = power( a, b)

		print( "\n\nThe result is: " + str(result) + "\n\nEXITING...")
		input()

