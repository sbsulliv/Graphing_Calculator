import math

while True:	
	print("\nChoose the math operation.\n\n0 -Addition\n1 - Subtraction\n2 - Multiplication\n3 - Division\n4 - Modulo\n5 - Raising to a power\n6 - Square root\n7 - Logarithm\n8 - Sine\n9 - Cosine\n10- Tangent\n")

	oper = input("\nYour option from the menu: ")
	
	if oper == "0":
		val1 = float(input("\nFirst value: "))
		val2 = float(input("\nSecond value: "))
		
		print("\nThe result is: " + str(val1 + val2) + "\n")
		
		back = input('\nGo back to the main menu? (y/n) ')
		
		if back == 'y':
			continue
		else:
			break
			
	elif oper == "1":
		val1 = float(input("\nFirst value: "))
		val2 = float(input("\nSecond value: "))
		
		print("\nThe result is: " + str(val1 - val2) + "\n")
		
		back = input('\nGo back to the main menu? (y/n) ')
		
		if back == 'y':
			continue
		else:
			break
			
	elif oper == "2":
		val1 = float(input("\nFirst value: "))
		val2 = float(input("\nSecond value: "))
		
		print("\nThe result is: " + str(val1 * val2) + "\n")
		
		back = input('\nGo back to the main menu? (y/n) ')
		
		if back == 'y':
			continue
		else:
			break
			
	elif oper == "3":
		val1 = float(input("\nFirst value: "))
		val2 = float(input("\nSecond value: "))
		
		print("\nThe result is: " + str(val1 / val2) + "\n")
		
		back = input('\nGo back to the main menu? (y/n) ')
		
		if back == 'y':
			continue
		else:
			break
			
	elif oper == "4":
		val1 = float(input("\nFirst value: "))
		val2 = float(input("\nSecond value: "))
		
		print("\nThe result is: " + str(val1 % val2) + "\n")
		
		back = input('\nGo back to the main menu? (y/n) ')
		
		if back == 'y':
			continue
		else:
			break	
			
	elif oper == "5":
		val1 = float(input("\nFirst value: "))
		val2 = float(input("\nSecond value: "))
		
		print("\nThe result is: " + str(math.pow(val1, val2)) + "\n")
		
		back = input('\nGo back to the main menu? (y/n) ')
		
		if back == 'y':
			continue
		else:
			break

	elif oper == "6":
		val1 = float(input("\nEnter value for extracting the square root: "))
		
		print("\nThe result is: " + str(math.sqrt(val1)) + "\n")
		
		back = input('\nGo back to the main menu? (y/n) ')
		
		if back == 'y':
			continue
		else:
			break			
			
	elif oper == "7":
		val1 = float(input("\nEnter the value for calculating the logarithm to base : "))
		
		print("\nThe result is: " + str(math.log(val1, 2)) + "\n")
		
		back = input('\nGo back to the main menu? (y/n) ')
		
		if back == 'y':
			continue
		else:
			break

	elif oper == "8":
		val1 = float(input("\nEnter value (in degrees)for calculating the sine : "))
		
		print("\nThe result is: " + str(math.sin(math.radians(val1))) + "\n")
		
		back = input('\nGo back to the main menu? (y/n) ')
		
		if back == 'y':
			continue
		else:
			break	
	elif oper == "9":
		val1 = float(input("\nEnter value (in degrees)for calculating the cosine : "))
		
		print("\nThe result is: " + str(math.cos(math.radians(val1))) + "\n")
		
		back = input('\nGo back to the main menu? (y/n) ')
		
		if back == 'y':
			continue
		else:
			break			

	elif oper == "10":
		val1 = float(input("\nEnter value (in degrees)for calculating the tangent : "))
		
		print("\nThe result is: " + str(math.tan(math.radians(val1))) + "\n")
		
		back = input('\nGo back to the main menu? (y/n) ')
		
		if back == 'y':
			continue
		else:
			break	

	else:
		print("\nInvalid option dumbass!\n")
		continue