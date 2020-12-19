

print ("Генератор чисел 'от' и 'до' ")
f = open(input("Введите название файла "), 'w')

for i in range (int(input ("Первое число ")),int(input("Последнее число "))+1):
	f.write (str(i)+ '\n')
	
f.close ()

