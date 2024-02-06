num1 = int(input("Give me a number: "))
operation = input("Select an operation: ")
num2 = int(input("Give me another number: "))

if operation == "+":
	total  = num1 + num2
	print (f"{num1} + {num2} = {total}")

elif operation == "-":
	total = num1 - num2
	print (f"{num1} - {num2} = {total}")

elif operation == "*": 
	total = num1 * num2
	print (f"{num1} * {num2} = {total}")

elif operation == "/":
	total = num1 / num2
	print (f"{num1} / {num2} = {total}")

elif operation == "**":
	total = num1 ** num2
	print (f"{num1} ** {num2} = {total}")

elif operation == "//":
	total = num1 // num2
	print (f"{num1} // {num2} = {total}")

elif operation == "%":
	total = num1 % num2
	print (f"{num1} % {num2} = {total}")
