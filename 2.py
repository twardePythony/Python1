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


#ad.1
def ad1():
	base = ["Ala", 1,233, "kot", {"PI": 3.14}, "e", 2.7183, "Mruczyslaw"]
	print base
	baseSort = sorted(base)
	print baseSort
	baseRev = sorted(base, reverse = True)
	print baseRev

#ad.1
#coding=utf-8

#ad.3
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

#ad.4
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

#ad.5
#serializacja obiektow typu pythonowego i instancji klas 

def ad5():
	import pickle
	"""Brak danych na temat roznicy miedzy dump vs dumps oraz load vs loads"""

	data = { "PI":3.14, "e":2.7183, "black":(255, 255, 255), 1:1, "kot":"Puszek"}
	#dump - zapisywanie do pliku
	pickle.dump(data, open("save.p", "wb"))

	#load - zaladowanie z pliku 
	data = pickle.load(open("save.p", "rb"))
	print data

	#klasa ktorej obiekt sobie zapiszemy
	class Example():
		def __init__(self, name, surname): 
			self.name = name
			self.surname = surname
		def __str__(self):
			return str(self.name, self.surname)


	with open("object.p", "wb") as output:
		e = Example("Name", "Surname")
		pickle.dump(e, output, pickle.HIGHEST_PROTOCOL)
	del e

	with open("object.p", "rb") as input:
		e = pickle.load(input)
	


########################################################################
#zadania domowe

def ZadDomAd2():
	#ad1 Uwaga bardzo brzydki niepythonowy kod no ale dziala
	l_krotek = [(1,), (255,255,255),("Ala", "kotek"), ("e", 2.7182),(3,3), (0,2,4,6,8,10, 12)]
	liczby = [x for x in l_krotek for j in x ]
	#print str(l_krotek[1][-1]).isdigit()

	def liczbyZlisty(l_krotek):
		l2 = []
		flaga = 0
		for i in l_krotek:
			suma = 0
			for j in i:
				if str(j).isdigit() :
					flaga = 1 
				else:
					flaga = 0
			if flaga == 1:
				l2.append((i))
				flaga = 0
		return l2
			
	l2 = liczbyZlisty(l_krotek)
	print l2

	#ad1.1
	l3 = []
	for i in l2:
		suma = 0
		for j in i:
			suma+=j
		if(suma % 2 == 0):
			l3.append((i))
			
	print "l3: ",l3

	#ad1.2
	l4= []
	flaga = 0
	for i in l2:
		for j in i:
			if j % 3 == 0:
				flaga = 1
			else:
				flaga = 0
				break
				
		if flaga == 1:
			l4.append((i))
			flaga = 0
	print "l4: ",l4

	#ad1.3
	l5 = []
	f = 0
	for i in l2:
		for j in i:
			if j % 3 == 0:
				f = 1
				break
		if f == 1:
			l5.append((i))
			f = 0
			
	print l5
	
##########################################
def ZadDomAd2():
	#ad2
	stringi = "0 Informatyk sie 3.14 cieszy; 255,255,255 gdy sie -123 uczy o stringach 2.7182 ".split()
	print stringi
	#ad2.1
	sameStringi = [x for x in stringi if x.isalpha()]
	print sameStringi
	#ad2.2
	print stringi
	print str(stringi[3]).isdigit()

	sameLiczby = [x for x in stringi if x.isalpha() == False]

	#trololo isdigit nie dziala dla FLOAT <----- Error Trololo Python
	sL = []
	for i in sameLiczby:
		if i.replace('.','').replace('-','').isdigit():
			sL.append(i)

	print sameLiczby
	print sL
	sl =[int(float(x)) for x in sL] #nie moge od razu zamienic na float :<
	print sl

#################################3
#ad.3
def ad3():
	import re
	def method2(txt):
		return '\n'.join([x for x in txt.split("\n") if x.strip()!=''])

	z = ''
	l = []

	with open("2.txt", "r" ) as file:
		for line in file:
			line = line.partition('#')[0]
			line = line.rstrip()
			if re.match(r'^\s*$', line): 
				line = ''
			else:
				l.append(line + '\n')
	file.close()

	print l
