mat = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
inp = 'X'

def check_win_status(row, column):   
    if (mat[row][0] == mat[row][1] == mat[row][2] != ' ') or (mat[0][column] == mat[1][column] == mat[2][column] != ' '):
        return True
    if (mat[0][0] == mat[1][1] == mat[2][2] != ' ') or (mat[0][2] == mat[1][1] == mat[2][0] != ' '):
        return True
    return False

def print_matrix():
    print(' _ _ _')
    print(f'|{mat[0][0]}|{mat[0][1]}|{mat[0][2]}|')
    print(' _ _ _')
    print(f'|{mat[1][0]}|{mat[1][1]}|{mat[1][2]}|')
    print(' _ _ _')
    print(f'|{mat[2][0]}|{mat[2][1]}|{mat[2][2]}|')

def take_input(inp):
    ur1 = int(input(f'Enter the row where you want to insert {inp}: '))
    uc1 = int(input(f'Enter the column where you want to insert {inp}: '))
    mat[ur1-1][uc1-1] = inp
    print_matrix()
    return [ur1-1, uc1-1]

print_matrix()
for i in range(9):
    l = take_input(inp)
    if check_win_status(l[0], l[1]):
        print('Won')
        break
    inp = 'X' if inp == 'O' else 'O'
else:
    print('draw')