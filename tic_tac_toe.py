def display_grid(grid):
    """
    displays the tic-tac-toe game grid
    """
    print(f"{grid[0]}|{grid[1]}|{grid[2]}")
    print("-+-+-")
    print(f"{grid[3]}|{grid[4]}|{grid[5]}")
    print("-+-+-")
    print(f"{grid[6]}|{grid[7]}|{grid[8]}")
    pass
def create_grid_list():
    grid = []
    for i in range(9):
        grid.append(i + 1)
    return grid
def did_you_win(grid):
    """
    determines if there is a winning game grid condition
    """
    #winning conditions:
    #123
    if grid[0] == grid[2] == grid[1]:
        
        return True
    #456
    if grid[3] == grid[4] == grid[5]:
        return True
    #789
    if grid[6] == grid[7] == grid[8]:
        return True
    #147
    if grid[6] == grid[3] == grid[0]:
        return True
    #258
    if grid[1] == grid[4] == grid[7]:
        return True
    #369
    if grid[2] == grid[5] == grid[8]:
        return True
    #159
    if grid[0] == grid[4] == grid[8]:
        return True
    #357
    if grid[2] == grid[4] == grid[6]:
        return True
    else:
        return False
def alternate_players(current):
    """
    makes the other player take a turn
    """
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"
def prompt_player(player, grid):
    """
    puts the current player's move onto the game grid
    """
    mark = input(f"{player}'s turn to choose a square (1-9)")
    mark = int(mark)
    grid[mark - 1] = player
def did_you_tie(grid):
    """
    determines if there is a tie game grid condition
    """
    for square in range(9):
        if grid[square] != "x" and grid[square] != "o":
            return False
    return True 

def main():
    grid = create_grid_list()
    player = alternate_players("")
    while did_you_win(grid) == False or did_you_tie(grid) == False:
        display_grid(grid)
        prompt_player(player, grid)
        player = alternate_players(player)
    display_grid(grid) 
    print("Good game. Thanks for playing!")  
    pass
if __name__ == "__main__":
    main()