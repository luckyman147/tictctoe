import math
import random

class player:
    def __init__(self,letter,name):
        #letter is x or o
        self.letter=letter
        self.name=name
    def getmove(self,game):

        pass
class HumanPlayer(player):
    def __init__(self, letter,name):
        super().__init__(letter,name)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-9): ')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        return val


class RandomComputerPlayer(player):
    def __init__(self, letter,name):
        super().__init__(letter,name)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square       

class RandomComputerPlayer(player):
    def __init__(self, letter,name):
        super().__init__(letter,name)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square       
class GenuisComputerPlayer(player):
    def __init__(self, letter,name):
       super().__init__(letter,name)
    def get_move(self,game):
        if len(game.available_moves())==9:
            square =random.choice(game.available_moves())
        else:
            #get the square based of minimax algorithm
            square=self.minimax(game,self.letter)['position']
        return square
    def minimax(self,state,player):
        max_player=self.letter 
        other_player='O' if player=='X' else 'X'
        if state.current_winner==other_player:
            #return position and score to keep track of the score
            return {'position':None,
            'score':1*(state.num_empty_squares()+1) if other_player==max_player else -1 *(state.num_empty_squares()+1)}
        elif not state.empty_squares():
            return {'position':None,'score':0}

        if player==max_player:
            #each score should maximize 
            best={'position':None,'score':-math.inf}        
        else:

            best={'position':None,'score':math.inf}        
        for possible_move in state.available_moves():
            #make a move
            state.make_move(possible_move,player)
            #recurse using minimax to simulate a game after making a move
            sim_score=self.minimax(state,other_player)
            #undo the move
            state.board[possible_move]=' '
            state.current_winner=None
            sim_score['position']=possible_move
            # update the dictionaries if necessary
            if player==max_player:  

            # i am trying to maximize the max_player             
                if sim_score['score']>best['score']:
                    best=sim_score
            else :
                #minimize the other player
                if sim_score['score']<best['score']:
                    best=sim_score        
        return best  
             
                        
        