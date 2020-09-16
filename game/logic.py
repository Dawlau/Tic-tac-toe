import constants
import pygame

coords = [[None, None, None],[None, None, None],[None, None, None]]

running = True
SP = 0 # singleplayer
MP = 0 # multiplayer
HS = 1 # aka home screen

# coords will be a 4D array that will contain the coordinates on the screen of the edges of every cell of the grid
def buildCoords():

    from graphics import verticalLine1, verticalLine2, horizontalLine1, horizontalLine2

    coords[0][0] = [[horizontalLine1.topleft[0], verticalLine1.topleft[1]],  # top left corner
                    [verticalLine1.topleft[0], horizontalLine1.topleft[1]]]  # bottom right corner

    coords[0][1] = [[verticalLine1.topright[0], verticalLine1.topright[1]], 
                    [verticalLine2.topleft[0], horizontalLine1.topleft[1]]]

    coords[0][2] = [[verticalLine2.topright[0], verticalLine2.topright[1]], 
                    [horizontalLine1.topright[0], horizontalLine1.topright[1]]]

    coords[1][0] = [[horizontalLine1.bottomleft[0], horizontalLine1.bottomleft[1]], 
                    [verticalLine1.topleft[0], horizontalLine2.topleft[1]]]

    coords[1][1] = [[verticalLine1.topright[0], horizontalLine1.bottomleft[1]], 
                    [verticalLine2.topleft[0], horizontalLine2.topleft[1]]]

    coords[1][2] = [[verticalLine2.topright[0], horizontalLine1.bottomleft[1]], 
                    [horizontalLine2.topright[0], horizontalLine2.topright[1]]]

    coords[2][0] = [list(horizontalLine2.bottomleft), 
                    list(verticalLine1.bottomleft)]

    coords[2][1] = [[verticalLine1.topright[0], horizontalLine2.bottomleft[1]], 
                    list(verticalLine2.bottomleft)]

    coords[2][2] = [[verticalLine2.topright[0], horizontalLine2.bottomright[1]], 
                    [horizontalLine2.bottomright[0], verticalLine2.bottomright[1]]]

def checkWinRows(grid):

    for r in range(3):
        cnt = 0
        ch = grid[r][0]

        if ch != '#':

            for c in range(3):
                if ch == grid[r][c]:
                    cnt += 1

            if cnt == 3:
                return True
    
    return False

def checkWinCols(grid):

    for c in range(3):
        cnt = 0
        ch = grid[0][c]

        if ch != '#':

            for r in range(3):
                if ch == grid[r][c]:
                    cnt += 1
            
            if cnt == 3:
                return True

    return False

def checkWinDiagonals(grid):

    cnt = 0
    ch = grid[0][0]

    if ch != '#':
        for i in range(3):
            if grid[i][i] == ch:
                cnt += 1

    if cnt == 3:
        return True

    cnt = 0
    ch = grid[0][2]

    if ch != '#':
        for i in range(3):
            if grid[i][3 - i - 1] == ch:
                cnt += 1

    if cnt == 3:
        return True

    return False

def checkWin(grid):
    return (checkWinRows(grid) | checkWinCols(grid) | checkWinDiagonals(grid))

def checkTie(grid):

    cnt = 0
    for r in range(3):
        for c in range(3):
            if grid[r][c] == '#':
                cnt += 1

    if cnt == 0:
        return True
    else:
        return False


# checks if x, y coordinates correspond to a cell
def getCell(x, y):

    for r in range(3):
        for c in range(3):
            if coords[r][c][0][0] < x < coords[r][c][1][0] and coords[r][c][0][1] < y < coords[r][c][1][1]:
                return r, c
    return None, None


def main():

    import graphics
    from homescreen import HomeScreen
    from singleplayer import Singleplayer
    from multiplayer import Multiplayer

    global running, HS, SP, MP

    homescreen = HomeScreen()
    singleplayer = Singleplayer()
    multiplayer = Multiplayer()

    while running:

        if HS:

            if HS == 1:
                homescreen.render(graphics.screen)
                HS += 1

            option = homescreen.getOption()

            if option == "SP":
                HS = 0
                MP = 0
                SP = 1
            elif option == "MP":
                HS = 0
                MP = 1
                SP = 0
        elif SP:
            if SP == 1:
                singleplayer.renderScreen(graphics.screen)
                singleplayer.resetGame(graphics.screen)
                SP += 1

            message = singleplayer.play(graphics.screen)

            if message == "Esc":
                SP = 0
                MP = 0
                HS = 1
        else:
            
            if MP == 1:
                multiplayer.renderScreen(graphics.screen)
                multiplayer.resetGame(graphics.screen)
                MP += 1

            message = multiplayer.play(graphics.screen)

            if message == "Esc":
                SP = 0
                MP = 0
                HS = 1