board = [
    [0,0,5,0,0,12,0,0,7,0,1,0],
    [6,8,0,12,0,1,7,0,0,0,4,0],
    [0,0,0,0,4,0,5,11,0,0,0,12],
    [10,0,0,0,12,0,8,0,0,0,9,0],
    [0,0,12,0,0,6,0,0,2,5,0,0],
    [0,1,4,9,0,0,0,10,0,0,12,6],
    [1,4,0,0,7,0,0,0,5,6,11,0],
    [0,0,8,5,0,0,2,0,0,10,0,0],
    [0,12,0,0,0,5,0,6,0,0,0,4],
    [9,0,0,0,10,3,0,5,0,0,0,0],
    [0,11,0,0,0,2,4,0,6,0,5,10],
    [0,2,0,8,0,0,11,0,0,3,0,0,0],

]
def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,13):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False

def valid(bo, num, pos):

    #check rows
    for i in range (len(bo[0])):
        if bo[pos[0]][i] == num and pos [1] !=i:
            return False

    #check columns
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    #check box
    box_x = pos[1] // 4
    box_y = pos [0] // 3

    for i in range (box_y * 3, box_y*3 + 3):
        for j in range(box_x * 4, box_x * 4 + 4):
            if bo[i][j] == num and (i,j) !=pos:
                return False

    return True

def print_board(bo):
    for i in range (len(bo)):
        if i % 3 == 0 and i !=0:
            print("= = = = = = = = = = = = = = = =")

        for j in range(len(bo[0])):
            if j % 4 == 0 and j !=0:
                print(" | ", end = "")

            if j == 11:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

def find_empty(bo):
    for i in range(len(bo)):
        for j in range (len(bo[0])):
            if bo[i][j] == 0:
                return (i,j)

    return None

solve(board)
print_board(board)

