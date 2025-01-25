

game = [[0]*3, [0]*3, [0]*3]


# def play(row, col, xo):
#     game[row][col] = xo
#     return game


elements = len([e for row in game for e in row if e != 0])

while elements < 9:
    turns = 0
    play = 'x' if not turns % 2 else 'o'
    row, col = [int(i)-1 for i in input().split(',')]
    while game[row][col] != 0:
        print("you can't play here, play again...")
        row, col = [int(i)-1 for i in input().split(',')]
    game[row][col] = play
    print(game)
    elements = len([e for row in game for e in row if e != 0])
    turns += 0

print("Game over")
print(game)
