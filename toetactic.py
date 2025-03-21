from random import choice
import copy

class Board:
    def __init__(self):
        self.game_state = [[0,0,0],[0,0,0],[0,0,0]]
        self.to_move = 1
    
    def __hash__(self):
        return hash(str(self.game_state) + str(self.to_move))
    
    def __eq__(self, other):
        return str(self.game_state) + str(self.to_move) == str(other.game_state) + str(other.to_move)
        
        

def solve_game(board):
    #takes in game board as 2d list of lists, returns a tuple containing the the best move
    #the move is a tuple containing the row and column of the move
    # 0 is empty, 1 is X, -1 is O
    if(board.game_state[1][1] == 0):
        return (1,1)
    #find an O with no X across from it (through the center)
    for i in range(3):
        for j in range(3):
            if(board.game_state[i][j] == -1 and board.game_state[2-i][2-j] == 0):
                return (2-i,2-j)
    #error
    return (-1,-1)
    
def random_move(board):
    #returns a random move (chooses random empty space)
    empty_spaces = []
    for i in range(3):
        for j in range(3):
            if(board.game_state[i][j] == 0):
                empty_spaces.append((i,j))
    return choice(empty_spaces)

def check_win(board):
    #returns 1 if X wins, -1 if O wins, 0 if no win
    #checks all rows, columns, and diagonals
    for i in range(3):
        if(board.game_state[i][0] == board.game_state[i][1] == board.game_state[i][2] != 0):
            return board.game_state[i][0] * -1
    for i in range(3):
        if(board.game_state[0][i] == board.game_state[1][i] == board.game_state[2][i] != 0):
            return board.game_state[0][i] * -1
    if(board.game_state[0][0] == board.game_state[1][1] == board.game_state[2][2] != 0):
        return board.game_state[0][0] * -1
    if(board.game_state[0][2] == board.game_state[1][1] == board.game_state[2][0] != 0):
        return board.game_state[0][2] * -1
    #check if there are any empty spaces
    for i in range(3):
        for j in range(3):
            if(board.game_state[i][j] == 0):
                return 5
    return 0
def generate_random_game():
    #returns a random game state
    states = []
    board = Board()
    states.append(copy.deepcopy(board))
    while(check_win(board) == 5):
        move = solve_game(board)
        board.game_state[move[0]][move[1]] = 1
        states.append(copy.deepcopy(board))
        if(check_win(board) != 5):
            break
        move = random_move(board)
        board.game_state[move[0]][move[1]] = -1
        states.append(copy.deepcopy(board))
    
    return states

def print_board(state):
    #returns a string representation of the board
    out = ""
    for i in range(3):
        for j in range(3):
            if(state[i][j] == 0):
                out += " "
            else:
                out += "X" if state[i][j] == 1 else "O"
        out += "\n"
    return out


def generate_data(num_games):
    dataset = set()
    for i in range(num_games):
        states = generate_random_game()
        for state in states:
            dataset.add(state)
    return dataset

