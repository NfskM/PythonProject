# Python - Τρίλιζα
import random

# Ο Πίνακας του παιχνιδιού
board = [0,1,2,3,4,5,6,7,8]


# Συνάρτηση που τυπώνει τον πίνακα
def show(board) :
    print (board[0], "|", board[1], "|", board[2])
    print ("-----------")
    print (board[3], "|", board[4], "|", board[5])
    print ("-----------")
    print (board[6], "|", board[7], "|", board[8])
    
    
#  Συνάρτηση που ελέγχει ποιος νίκησε σε κάθε παρτίδα     
def mlk() :
    if board[0]==board[3] and board[3]==board[6]:
        print ("Strike!")
        mlk=False
        
    elif board[1]==board[4] and board[4]==board[7]:
        print ("Strike!")
        mlk=False
        
    elif board[2]==board[5] and board[5]==board[8]:
        print("Strike!")
        mlk=False
    
    elif board[0]==board[1] and board[1]==board[2]:
        print ("Strike!")
        mlk=False
    
    elif board[3]==board[4] and board[4]==board[5]:
        print ("Strike!")
        mlk=False
    
    elif board[6]==board[7] and board[7]==board[8]:
        print ("Strike!")
        mlk=False
        
    elif board[0]==board[4] and board[4]==board[8]:
        print ("Strike!")
        mlk=False
    
    elif board[2]==board[4] and board[4]==board[6]:
        print ("Strike!")
        mlk=False
    else:
       
        mlk=True
        
    return mlk  

#Αρχικοποιώ το i για να κάνει συγκεκριμενες επαναλήψεις 
i=0        
print ("You play as 'x' and your opponent plays as 'o'.")  
f=mlk()
while (i<10 and f):
    i=i+1
    t = int(input("Select a spot: "))
    while (t>=9):
        t = int(input("The number has to be below 9. Please select again: "))
    if board[t] != "x" and board[t] !="o":
        board[t] = "x"
        finding = True
        while (finding):    
         random.seed() 
         opponent =  random.randint(0,8)
         
         if board[opponent] != "o" and board[opponent] != "x":
                    board[opponent] = "o"
                    finding = False
                    show(board)
        
    else: 
        print ("This spot is taken !")
        show(board)
    f=mlk()
