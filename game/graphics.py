import pygame
import constants
import logic



def setup():

    global screen

    pygame.init()
    screen = pygame.display.set_mode([constants.height, constants.width])
    pygame.display.set_caption("Tic-Tac-Toe")

    init_Fonts()



def init_Fonts():

    pygame.font.init()

    global TMR30

    TMR30 = pygame.font.SysFont('Times New Roman', 30)



def drawGrid(screen):

    global verticalLine1, verticalLine2, horizontalLine1, horizontalLine2

    verticalLine1 = pygame.draw.line(screen, 
                                     constants.black, 
                                    [constants.height // 2 - constants.gridSize // 5, constants.width // 2 - constants.gridSize // 2], 
                                    [constants.height // 2 - constants.gridSize // 5, constants.width // 2 + constants.gridSize // 2 - 1], 
                                     constants.lineWidth)

    verticalLine2 = pygame.draw.line(screen, 
                                     constants.black, 
                                    [verticalLine1.topright[0] + constants.gridSize // 3, verticalLine1.topright[1]], 
                                    [verticalLine1.bottomright[0] + constants.gridSize // 3, verticalLine1.bottomright[1]], 
                                     constants.lineWidth)

    horizontalLine1 = pygame.draw.line(screen, 
                                       constants.black, 
                                      [verticalLine1.topleft[0] - constants.gridSize // 3, verticalLine1.topleft[1] + constants.gridSize // 3], 
                                      [verticalLine2.topright[0] + constants.gridSize // 3, verticalLine2.topright[1] + constants.gridSize // 3], 
                                       constants.lineWidth)

    horizontalLine2 = pygame.draw.line(screen,
                                       constants.black, 
                                      [horizontalLine1.bottomleft[0], horizontalLine1.bottomleft[1] + constants.gridSize // 3], 
                                      [horizontalLine1.bottomright[0], horizontalLine1.bottomright[1] + constants.gridSize // 3], 
                                       constants.lineWidth)

    from logic import buildCoords
    buildCoords()

    



# call if you want to draw an X with the edges from logic.coords[row][col]
def drawX(screen, grid, row, col):

    grid[row][col] = 'X'

    diff = constants.cellSize // 6

    topleftx = logic.coords[row][col][0][0]
    toplefty = logic.coords[row][col][0][1]

    botrightx = logic.coords[row][col][1][0]
    botrighty = logic.coords[row][col][1][1]

    topleftx += diff
    toplefty += diff

    botrightx -= diff
    botrighty -= diff

    pygame.draw.line(screen, 
                     constants.black, 
                    [topleftx, toplefty], 
                    [botrightx, botrighty], 
                     constants.lineWidth)

    topright = [botrightx, toplefty]
    botleft = [topleftx, botrighty]

    pygame.draw.line(screen, constants.black, topright, botleft, constants.lineWidth)

    



# call if you want to draw an O with the edges from logic.coords[row][col]
def drawO(screen, grid, row, col):

    grid[row][col] = 'O'
    
    topleftx = logic.coords[row][col][0][0]
    toplefty = logic.coords[row][col][0][1]
    botrightx = logic.coords[row][col][1][0]
    botrighty = logic.coords[row][col][1][1]

    xdiff = constants.cellSize // 4
    ydiff = constants.cellSize // 10

    topleftx += xdiff
    toplefty += ydiff
    
    dimensions = botrightx - topleftx - xdiff, botrighty - toplefty - ydiff

    pygame.draw.ellipse(screen, 
                        constants.black, 
                        ([topleftx, toplefty], dimensions), 
                        constants.lineWidth)
    
    



def renderControls(screen):

    restartWidth, restartHeight = TMR30.size(constants.restartText)
    text = TMR30.render(constants.restartText, True, constants.black)
    screen.blit(text, (constants.width - restartWidth, constants.height - restartHeight))

    topleftRestartText = [constants.width - restartWidth, constants.height - restartHeight]
    quitWidth, quitHeight = TMR30.size(constants.quitText)
    text = TMR30.render(constants.quitText, True, constants.black)
    screen.blit(text, [topleftRestartText[0], topleftRestartText[1] - quitHeight])

    text = TMR30.render(constants.escText, True, constants.black)
    screen.blit(text, (0, 0))
    



def renderMsgAboveGrid(screen, message):

    textWidth, textHeight = TMR30.size(message)
    text = TMR30.render(message, True, constants.black)

    screen.blit(text, (logic.coords[0][0][0][0] + (constants.gridSize - textWidth) // 2 + 1, logic.coords[0][0][0][1] - textHeight))