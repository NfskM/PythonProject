#Άκσηση 3 
#Π18099
#Μαστροδήμα Ναυσικά
# -*- coding: utf-8 -*-
nfsk=open("e1.py","r")
lines=nfsk.readlines()
nfsk.close()
#Ο κώδικας δουλεύει μόνο για #
for line in lines:
	if "#" in line:
		#Ελέγχει αν η γραμμή αρχίζει από "#";
		l=line.strip()
		if l[0]!="#": 
  
			tmp=line.split("#")
			
			x=tmp[0].count("'")
			y=tmp[0].count('"')
			
			if x%2==1 or y%2==1:
				print (line)
			else:
				print (line.split("#")[0])
	else:
		print (line)
