

f = open(input("Введите точное название сгенерированного файла "))


for line in f:
	print (f"У номера места {line} купе #", (lambda n: (-(n//-4)))(int(line)))
	
