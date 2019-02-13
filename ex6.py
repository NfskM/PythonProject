#Ναρκαλιευτής

import random

board = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]


def show(board) :
    print ("--------------------------")
    print (board[0], "|", board[1], "|", board[2], "|", board[3])
    print ("--------------------------")
    print (board[4], "|", board[5], "|", board[6], "|", board[7])
    print ("--------------------------")
    print (board[8], "|", board[9], "|", board[10], "|", board[11])
    print ("--------------------------")
    print (board[12], "|", board[13], "|", board[14], "|", board[15])
    print ("--------------------------")
    print (board[16], "|", board[17], "|", board[18], "|", board[19])
    print ("--------------------------")
    
y = int(input("Select number of bombs: "))
while (y>20):
    y = int(input("You can't bomb without thinking! Bombs can't be over 20. Please select again: "))
        
for i in range(y):   
    bomb =  random.randint(0,19)
   
    while (board[bomb] == "bomb"):
        bomb =  random.randint(0,19)
    board[bomb] = "bomb"
    #print (bomb)
show(board)
       
