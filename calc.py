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
	if num2 == 0:
		print("You cannot divide by zero, the answer is undefined.")
	else:
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
else:
	print("Invalid operation. Acceptable operations are +, -, *, /, **, //, %.")