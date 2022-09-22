import copy

from cgi import test


def vhodnaF():
	"""test = 1
	l1 = [1, "Bostjan", True, 0.004, test, [1, 0.04]]	#seznam
	print(l1[5])

	d1 = {"ABC":123, 17:"Nekej"}	#dictionary, vrednosti morejo met svoje kljuce Kljuc:Vrednost
	print(d1["ABC"])

	t1 = (1, 7, 4,)	#tuple, samo enak tip spremenljivk, po definiranju ne mores vec spreminjat

	l1[2] = False
	print(l1)

	l1.append(1111)
	print(l1)

	l1.pop()
	print(l1)

	l1.insert(3, "vnisjud")
	l1.remove(1)

	print(l1.index("vnisjud"))

	d1["vnisjud"] = 125346"""


	l1 = [1, 2, 4]

	l2 = copy.deepcopy(l1)

	l2.append(7)

	print(l1)
	print(l2)



if __name__ == "__main__":
	vhodnaF()