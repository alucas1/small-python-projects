# Variable initialization
border = "---------"
x_wins = False
o_wins = False
impossible = False
valid_input = False
x_turn = True

# Print game board initially
game_layout_matrix = [[" ", " ", " "],
                      [" ", " ", " "],
                      [" ", " ", " "]]

print(border)
print('|', *game_layout_matrix[0], '|', sep=' ')
print('|', *game_layout_matrix[1], '|', sep=' ')
print('|', *game_layout_matrix[2], '|', sep=' ')
print(border)

# Game loop
for turn in range(0, 9):
    # Check user input
    valid_input = False
    while valid_input is False:
        user_input = input()
        try:
            row = int(user_input[0])
            col = int(user_input[2])
        except ValueError:
            print("You should enter numbers!")
        else:
            if 0 < row <= 3 and 0 < col <= 3:
                if game_layout_matrix[row - 1][col - 1] == ' ':
                    game_layout_matrix[row - 1][col - 1] = 'X' if x_turn else 'O'
                    x_turn = not x_turn
                    valid_input = True
                else:
                    print("This cell is occupied! Choose another one!")
                continue
            else:
                print("Coordinates should be from 1 to 3!")

    # Print updated board
    print(border)
    print('|', *game_layout_matrix[0], '|', sep=' ')
    print('|', *game_layout_matrix[1], '|', sep=' ')
    print('|', *game_layout_matrix[2], '|', sep=' ')
    print(border)

    # Grab all lines
    horizontals = [''.join(game_layout_matrix[0]), ''.join(game_layout_matrix[1]), ''.join(game_layout_matrix[2])]
    verticals = [game_layout_matrix[0][0] + game_layout_matrix[1][0] + game_layout_matrix[2][0],
                 game_layout_matrix[0][1] + game_layout_matrix[1][1] + game_layout_matrix[2][1],
                 game_layout_matrix[0][2] + game_layout_matrix[1][2] + game_layout_matrix[2][2]]
    diagonals = [game_layout_matrix[0][0] + game_layout_matrix[1][1] + game_layout_matrix[2][2],
                 game_layout_matrix[0][2] + game_layout_matrix[1][1] + game_layout_matrix[2][0]]

    # Check winning conditions
    if 'XXX' in [*horizontals, *verticals, *diagonals]:
        x_wins = True
        break
    if 'OOO' in [*horizontals, *verticals, *diagonals]:
        o_wins = True
        break

if x_wins:
    print("X wins")
elif o_wins:
    print("O wins")
else:
    print("Draw")

