class Board:
    def __init__(self):
        self.board = [['E', 'E', 'E'], ['E', 'E', 'E'], ['E', 'E', 'E']]
        self.turn = "unknown"
        self.state = "unknown"
    def print_board (self):
        for i in self.board:
            print(i)
    def test_Board(self):
        print("Testing Board")
        print(self.board)
        print(self.turn)
        print(self.state)
        self.print_board()
#game = Board()
#game.test_Board()
