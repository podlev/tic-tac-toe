import random


class Board:
    def __init__(self):
        self.field = [
            ['.', '.', '.'],
            ['.', '.', '.'],
            ['.', '.', '.']
        ]

    def __str__(self):
        lines = []
        for row in self.field:
            lines.append(' | '.join(row))
        return '\n—————————\n'.join(lines)

    def make_move(self, row, col, symbol):
        if self.field[row][col] == '.':
            self.field[row][col] = symbol
            return True
        return False

    def check_winner(self, symbol):
        for i in range(3):
            if self.field[i][0] == symbol and self.field[i][1] == symbol and self.field[i][2] == symbol:
                return True

            if self.field[0][i] == symbol and self.field[1][i] == symbol and self.field[2][i] == symbol:
                return True

        if self.field[0][0] == symbol and self.field[1][1] == symbol and self.field[2][2] == symbol:
            return True

        if self.field[0][2] == symbol and self.field[1][1] == symbol and self.field[2][0] == symbol:
            return True

        return False

    def is_full(self):
        for row in self.field:
            for cell in row:
                if cell == '.':
                    return False
        return True


class Game:
    def __init__(self):
        self.board = Board()
        self.current_player = 'X'

    def switch_player(self):
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'

    def play(self):
        while True:
            if self.current_player == 'X':
                row, col = map(int, input().split())
            else:
                free_cells = [(row, col) for row in range(3) for col in range(3) if self.board.field[row][col] == '.']
                row, col = random.choice(free_cells)

            if self.board.make_move(row, col, self.current_player):
                print(self.board)

                if self.board.check_winner(self.current_player):
                    print(f'Победил {self.current_player}')
                    break

                if self.board.is_full():
                    print('Ничья')
                    break

                self.switch_player()


game = Game()
game.play()
