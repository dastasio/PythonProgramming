
def getNum():
	x = input('Give me a number: ')
	return int(x)

class calc:
	
	def addition( x, y):
		m_sum = x + y
		print( m_sum)

	def subtraction( x, y):
		m_diff = x - y
		print( m_diff)

	def multiplication( x, y):
		m_prod = x * y
		print( m_prod)

	def division( x, y):
		m_quoz = x / y
		print( m_quoz)
	
	def printMenu():
		print('1.Addition\n2.Subtraction\n3.Multiplication\n4.Division')
		choice = input( '\nWhat operation would you like? ')
		return int(choice)

if __name__ == '__main__':
	k = calc.printMenu()
	x = getNum()
	y = getNum()
	if k == 1:
		calc.addition(x, y)
	elif k == 2:
		calc.subtraction(x, y)
	elif k == 3:
		calc.multiplication(x, y)
	elif k == 4:
		calc.division(x, y)
	else:
		print( 'Please choose a number between 1 and 4!', k)

