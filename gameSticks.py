from sticks import humanPlayer,robotPlayer

def game(nbSt,firstPlayer,secondPlayer):
    turn=1
    print("le jeu commence")
    while nbSt>5:
        print('Le nombre de sticks :',nbSt)
        if turn ==1:
            print( firstPlayer.name ,"should play ")
            nbSt=firstPlayer.getmove(nbSt)
            turn=2
        else:
            print( secondPlayer.name ,"should play ")

            nbSt=secondPlayer.getmove(nbSt)
            turn =1
    if  nbSt==5 :
        print('Le nombre de sticks :',nbSt)

        if turn==1:
            print(secondPlayer.name,'win')
        else:
            print(firstPlayer.name,'win')
    else:   
        print('Le nombre de sticks :',nbSt)
        
        if turn==1:
            print(firstPlayer.name,'win')
        else:
            print(secondPlayer.name,'win')         

firstplayet=humanPlayer('iyed')
secplayet=robotPlayer("robot")
game(10,firstplayet,secplayet)