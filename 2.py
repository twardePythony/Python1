#coding=utf-8 #

"""
1. Sortowanie list
2. kodowanie stringow, typ unicode, #coding=utf8
3. Slowniki, znajdowanie wartosci dla klucza, metody: get, keys, values, len
4. Otwieranie i zamykanie pliku, mody "w", "r", "a", intrukcje:
	read, readlines, redline, write, petlna for po pliku
5. Serializacja - modul pickle, metody: dump. load, dumps, loads


ZADANIE DOMOWE:
1.Dla listy krotek:
1.1 Pozostaw w liscie tylko krotki, ktorych suma jest parzysta
1.2 Pozostaw w liscie tylko krotki, w ktorych wszystkie liczby sa podzielne przez 3
1.3 Pozostaw w liscie tylko krotki, w ktorych istnieje liczba podzielna przez 3
2.Dla listy stringow
2.1 Oczysc elementy z nieliter
2.2 Oczysc elementy z niecyfr, pozostaw niepuste i przeksztalc do integerow
3.Dla pliku z komentarzami po # i z pustymi liniami
3.1 Wczytaj do listy linie z wycietymi komentarzami i bez znakow bialych na koncach.
	W liscie ma nie byc pustych linii
"""


#ad1.
def ad1():
	base = ["Ala", 1,233, "kot", {"PI": 3.14}, "e", 2.7183, "Mruczyslaw"]
	print base
	baseSort = sorted(base)
	print baseSort
	baseRev = sorted(base, reverse = True)
	print baseRev

#ad2.
#coding=utf-8

#ad3.
def ad3():
	n = 0
	d = {"Ala":"kotek", "PI":3.14, 0: "zero", 1:1, 2.7183: "e", n : None}
	for key in d:
		print "key: ", key, " : value: ", d[key]
		
	d["Asia"] = "Biska"
	print d
	del d[0]
	print d
	#get()
	x = "PI"
	print d[x]
	d.get(x)
	#keys()
	print d.keys()
	for k in d.keys():
		print d[k]
	#values
	print d.values()
	#len()
	print len(d)
	d.clear()
	print d

#ad4.
	def ad4():
	myfile = open("Text.txt", "w")
	myfile.write('Ala ma kota\n')
	myfile.write("Jednak nie\nBo to kot ma Ale\n <3")
	myfile.close()


	myfile = open("Text.txt", "r") #dla binarnych byloby rb
	print myfile.read()  #wczytanie wszystkiego na raz do lancucha znakow

	#petla for - uzycie iteratorow plikow, a nie wczytywania
	for line in myfile:
		print line, #przecinek zeby nie dodawal nowej linii
	#Uwaga petla for zwraca itertor !!!


	print myfile.readline()
	print myfile.readlines()
	myfile.close()

	myfile = open("Text.txt", "a") #dopisywanie - nie mozna czytac w tym trybie
	myfile.write("<3 <3 <3 <3 <3 <3 <3")
	myfile.close()

	myfile = open("Text.txt", "r")
	#readlines() nie formatuje stringa tylko wypisuje '\n'
	print myfile.readlines() 

	##Lepszy sposob na otwieranie pliku - bezpieczniejszy
	# -file.close() jest automatycznie wywolywana 
	with open("2.txt") as file:	# Use file to refer to the file object
		data = file.read()
		#do something with data
		print data

	d = {"a":"A", "e":2.7182, 1:111}
	binarData = open('data.bin', 'wb') #wb - write binary
	binarData.write(str(bin(127)+ '\n')) #zapisuje tylko stringi
	binarData.write(str(d))
	binarData.close()

	binarData = open('data.bin', 'rb')
	print binarData.read()

 
