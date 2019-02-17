#Άσκηση 12
#Π18099
#Ναυσικά Μαστροδήμα
#2019

#Άνοιγμα αρχείου και μετατροπή αυτού σε λίστα
file = open("test.txt", "r")
list1=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
frequency=[0]
nf=[]

for i in range(26):
    frequency.append(0)

with open("test.txt", "r") as file:
    for i in file.read():
        nf.append(i)
#Μετατροπή χαρακτήρων
nf = [element.lower() for element in nf];
# Στατιστικά εμφάνισης κάθε γράμματος
for i in range(len(nf)):
    for j in range(len(list1)):
        if(nf[i]==list1[j]):
            frequency[j]=frequency[j]+1
#Εύρεση λιγότερο εμφανιζόμενου και περισσότερο εμφανιζόμενου χαρακτήρα
while(i<=len(frequency)):
    if(frequency!=0):
        max=0
        min=i
    else:
        i=i+1

for i in range(len(frequency)):
    if((frequency[i]>frequency[max])):
        max=i
    if((frequency[i]<frequency[min])and(frequency[i]!=0)):
        min=i
#Αντιστροφή Χαρακτήρων
for i in range(len(nf)):
    if(nf[i]==list1[max]):
        nf[i]=list1[min]
    if(nf[i]==list1[min]):
        nf[i]=list1[max]
#Μετατροπή λίστας σε string και εκτύπωση κειμένου και στατιστικά
nf = ''.join(nf)
print(nf.upper())
print(frequency)
