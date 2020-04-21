# Sudoku 
Sudoku (数独,  originally called "Number Place") is a well known number-placement puzzle. It's history reaches 19th century.

According to Guiness World Records the fastest sudoku was completed in 1 min 23.93 sec. But what if each of us could do it in just a few seconds?


### Python solver 🤯 🕵

A simple python script is able to complete a sudoku just in few seconds. It uses [backtracking algorithm](https://en.wikipedia.org/wiki/Backtracking) which tests all possible paths till a solution is found or all paths have been tested.

```python
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
                
```

### Pygame app



![alt text](https://github.com/lmarcinski/sudoku_12x12/blob/master/newfoldername/sudoku12x12.png)
