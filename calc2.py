
class calc:
	res = 0

	def sum( num1, num2):
		calc.res = num1 + num2
	
	def dif( num1, num2):
		calc.res = num1 - num2

	def mult( num1, num2):
		calc.res = num1 * num2
	
	def div( num1, num2):
		calc.res = num1 / num2
	
	def printMenu():
		print ("WELCOME!\n\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n")
		print ("Please choose an option: ")
		choice = int(input())
		print( "number 1: ")
		n1 = int(input())
		print( "number 2: ")
		n2 = int(input())
		if choice == 1:
			calc.sum( n1, n2)
		elif choice == 2:
			calc.dif( n1, n2)
		elif choice == 3:
			calc.mult( n1, n2)
		elif choice == 4:
			calc.div( n1, n2)
		else:
			print( "Please choose a correct option!")
			input()
			print( "\n\n\n\n\n\n\n\n\n")

		print(calc.res)


calc.printMenu()
