

while True:
	operacija = input("Izberite eno izmed operacij: +, -, *, / :")
	print("Izbrana operacija: " + str(operacija))

	a = input("Izberite prvo poljubno stevilo: ")
	b = input("Izberite drugo poljubno stevilo: ")

	if operacija == "+":
		print("Rezultat je: " + str(a+b))
	elif operacija == "-":
		print("Rezultat je: " + str(a-b))
	elif operacija == "*":
		print("Rezultat je: " + str(a*b))
	elif operacija == "/":
		print("Rezultat je: " + str(a/b))

	nadaljuj = input("Zelite nadaljevati? (Da/Ne)")
	if nadaljuj == "Ne":
		break