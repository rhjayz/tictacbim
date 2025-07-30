EMPTY = ""
PLAYER_X = "X"
PLAYER_O = "O"

class GameLogic:
    def __init__(self):
        self.starting_player = "X"
        self.current_player = self.starting_player
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.winner = None

    def make_move(self, row, col):
        if self.board[row][col] == "" and self.winner is None:
            self.board[row][col] = self.current_player
            self.check_winner()
            if not self.winner:
                self.toggle_player()
            return True
        return False
    
    def toggle_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        lines = []

        lines.extend(self.board)
        lines.extend([[self.board[r][c] for r in range(3)] for c in range(3)])

        lines.append([self.board[i][i] for i in range(3)])
        lines.append([self.board[i][2 - i] for i in range(3)])

        for line in lines:
            if line[0] != "" and all(cell == line[0] for cell in line):
                self.winner = line[0]
                break

    def is_draw(self):
       return all(cell != "" for row in self.board for cell in row) and self.winner is None
    
    def reset(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]

        self. starting_player = "O" if self.starting_player == "X" else "X"
        self.current_player = self.starting_player

        self.winner = None