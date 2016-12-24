class GameEngine(object):
    def __init__(self):
        self.board = [['E', 'E', 'E'], ['E', 'E', 'E'], ['E', 'E', 'E']]
        #self.board = [['O', 'X', 'X'],['X', 'O', 'O'],['X', 'O', 'E']]#test cats game
        self.turn = "unknown"
        self.state = "unknown"
    def print_board (self):
        for i in self.board:
            print(i)
    def decide_who_goes_first(self):
        import random
        if random.randrange(2) == 0:
            #print("O gets to go first")
            self.turn = "O"
        else:
            #print("X gets to go first")
            self.turn = "X"
        self.state = "play"
        return self.turn
    def check_winner(self):
        for i in ["X","O"]:
            for num in range(3):
                if i == self.board[num][0] and i ==  self.board[num][1] and i == self.board[num][2]:
                    #print(i, "WINS")
                    self.state = i + " WINS"
                elif i == self.board[0][num] and i ==  self.board[1][num] and i == self.board[2][num]:
                    print(i, "WINS")
                    self.state = i + " WINS"
                elif i == self.board[0][0] and i ==  self.board[1][1] and i == self.board[2][2]:
                    #print(i, "WINS")
                    self.state = i + " WINS"
                elif i == self.board[0][2] and i ==  self.board[1][1] and i == self.board[2][0]:
                    #print(i, "WINS")
                    self.state = i + " WINS"
        #print(self.game_state)
        return False
    def check_cats(self):
        count = 0
        for j in range(3):
            for k in range(3):
                if self.board[j][k] == "E":
                    count += 1
        if (count == 0):
            self.state = "cats"
    def do_turn(self, yPos, xPos):#remember down then accrsoss
        if (self.state == "play"):
            #print("It is " + self.turn + "'s turn")
            if self.board[yPos][xPos] == "E":
                self.board[yPos][xPos] = self.turn
            if self.turn == "X":
                self.turn = "O"
            else:
                self.turn = "X"
        else:
            return("GAME OVER")#should I return False
        self.check_cats()
        self.check_winner()
#game = GameEngine()
#game.test_Board()
#game.test_GameEngine()