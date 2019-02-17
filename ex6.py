#Άσκηση_6
#Π18099
#Ναυσικά Μαστροδήμα
#2019
#Ναρκαλιευτής
import random
rows=int(input('Give me the number of the rows: '))
while rows<0:
	print ('The rows cannot be negative number stupid!!!!')
	rows=int(input('Give me the number of the rows, right this time: '))
columns=int(input('Give me the number of the columns: '))
while columns<0:
	print ('The rows cannot be negative number stupid!!!!')
	columns=int(input('Give me the numder of the columns, again: '))
tbl=[]
for i in range(rows):
		rows1=[]
		for j in range(columns):
			so=random.randrange(0,9);
			rows1.append(so)
		tbl.append(rows1)

bombs=int(input('Give me the number of the bombs: '))
while (bombs<0 or bombs>rows*columns):
	print ('The rows cannot be negative number and bombs bigger than the dimension of the table stupid!!!!')
	bombs=int(input('Give me the numbers of the bombs: '))
for j in range(0,bombs):
	F=False
	while F==False:
		rndm1=random.randrange(0,rows)
		rndm2=random.randrange(0,columns)
		if tbl[rndm1][rndm2]!="|>":
			tbl[rndm1][rndm2]="|>"
			F=True
            
for xs in tbl:
   print(" ".join(map(str, xs)).center(100))

