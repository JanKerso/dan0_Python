import time
#from time import sleep
#import time as t

a = 54
b = 82
a + b

print("Sestevek je "+str(a+b))

"""
in tudi to je komentar
"""

if a>b:
	print("a je vecji od b!") #<= == is is not in
	#to je komentar
elif a<b:
	print("a je manjsi od b!")
else:
	print("noben pogoj ni izpolnjen!")


while True:
	a += 1
	print("a je : "+str(a))
	#time.sleep(0.1)
	if a > b:
		break


vhod = input("Vnesi najljubso stevilko: ")
print("vasa stevilka je: " + str(vhod))