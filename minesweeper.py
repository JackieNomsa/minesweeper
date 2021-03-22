# importing random library 
import random

# You may create additional functions here:
def board( X, Y): # X no. bombs, Y one side grid size

    my_grid = [[0 for row in range(Y)] for column in range(Y)]
    my_bomb_pos = list()
    

    for num in range(X):
        x = random.randint(0,Y-1)
        y = random.randint(0,Y-1)
        my_grid[y][x] = 'X'
        my_bomb_pos.append([x,y])
        # placing the number of bombs adjacent

        #place bomb on the middle right
        if (x >=0 and x <= Y-2) and (y >= 0 and y <= Y-1):
            if my_grid[y][x+1] != 'X':
                my_grid[y][x+1] += 1 
       
       #place bomb on the middle left
        if (x >=1 and x <= Y-1) and (y >= 0 and y <= Y-1):
            if my_grid[y][x-1] != 'X':
                my_grid[y][x-1] += 1 

        #place bomb on the top left
        if (x >= 1 and x <= Y-1) and (y >= 1 and y <= Y-1):
            if my_grid[y-1][x-1] != 'X':
                my_grid[y-1][x-1] += 1
 
        #place bomb on the top right
        if (x >= 0 and x <= Y-2) and (y >= 1 and y <= Y-1):
            if my_grid[y-1][x+1] != 'X':
                my_grid[y-1][x+1] += 1 
        #place bomb on the top center
        if (x >= 0 and x <= Y-1) and (y >= 1 and y <= Y-1):
            if my_grid[y-1][x] != 'X':
                my_grid[y-1][x] += 1

        #place bomb on the bottom right
        if (x >=0 and x <= Y-2) and (y >= 0 and y <= Y-2):
            if my_grid[y+1][x+1] != 'X':
                my_grid[y+1][x+1] += 1 

        #place bomb on the bottom left
        if (x >= 1 and x <= Y-1) and (y >= 0 and y <= Y-2):
            if my_grid[y+1][x-1] != 'X':
                my_grid[y+1][x-1] += 1 

        #place bomb on the bottom center
        if (x >= 0 and x <= Y-1) and (y >= 0 and y <= Y-2):
            if my_grid[y+1][x] != 'X':
                my_grid[y+1][x] += 1 

           
    for row in my_grid:
        print(' |', ' | '.join(str(" ").replace('0',' ') for cell in row), '| ')
        print()

    play(my_bomb_pos,my_grid)
    return my_grid
    

#write the number of rows and columns 
number_grids = int(input('Please enter the number of rows and columns you want on your grid: '))
number_bombs = int(input(f'Please enter the number of bombs you want present in your game (must be less that {number_grids**2})'))


def play(my_bomb_pos,my_grid):
    row = int(input('choose row to dig: '))
    column = int(input('choose column to dig: '))

    userinput = [row, column]
    

    for lis in my_bomb_pos:
        if userinput in my_bomb_pos:
            print('Game over!!')

            for row in my_grid:
                print(' |', ' | '.join(str(cell).replace('0',' ') for cell in row), '| ')
                print()

            exit()
        else:
            # for row in my_grid:
            #     for cell in row:
            #         if my_grid.index(cell) in userinput:
            #             print(cell)
            #         else:
            #             print(' ')
            #     print()
            
            return play(my_bomb_pos, my_grid)


# Additional Functions above this comment

# Implement your Minesweeper Solution Below:
 

#     pass
#     #Edit the code Above Here
# #play Function Ends Here

if __name__=='__main__':
    board(number_bombs,number_grids)