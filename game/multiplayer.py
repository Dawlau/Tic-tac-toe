class Multiplayer():
    
    def __init__(self):
        self.resetVars()


    def resetVars(self):

        self.player = 0
        self.renderEndGameMessage = False

        import constants
        import copy

        self.grid = copy.deepcopy(constants.defaultGrid)
        self.win = False
        self.tie = False

    
    def resetGame(self, screen):

        self.resetVars()
        self.renderScreen(screen)


    def renderScreen(self, screen):

        import graphics
        from constants import white

        screen.fill(white)
        graphics.drawGrid(screen)
        graphics.renderControls(graphics.screen)

        for row in range(3):
            for col in range(3):
                if self.grid[row][col] == "X":
                    graphics.drawX(screen, self.grid, row, col)
                elif self.grid[row][col] == "O":
                    graphics.drawO(screen, self.grid, row, col)

        if not self.win and not self.tie:
            graphics.renderMsgAboveGrid(screen, ("O" if self.player == 1 else "X") + "'s turn")


    def endGame(self, screen):

        import graphics

        if (self.win or self.tie) and not self.renderEndGameMessage:

            self.renderScreen(screen)
            self.renderEndGameMessage = True
            
            message = None

            if self.win:
                message = ("O" if self.player == 0 else "X") + " won!"
            else:
                message = "It's a tie!"

            graphics.renderMsgAboveGrid(screen, message)

    
    def move(self, screen, row, col):

        import graphics

        if row == None:
            return
                
        if self.grid[row][col] != "#":
            return
        
        if self.player == 0:
            graphics.drawX(screen, self.grid, row, col)
            self.player ^= 1
            self.renderScreen(screen)
        else:
            graphics.drawO(screen, self.grid, row, col)
            self.player ^= 1
            self.renderScreen(screen)



    def play(self, screen):

        import pygame, logic, graphics

        for event in pygame.event.get():

            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_q]:
                logic.running = False
                break
            elif pygame.key.get_pressed()[pygame.K_r]:
                self.resetGame(screen)
            elif pygame.key.get_pressed()[pygame.K_ESCAPE]:
                return "Esc"
            elif (not self.win and not self.tie) and event.type == pygame.MOUSEBUTTONDOWN:
                clickCoords = event.pos
                
                row, col = logic.getCell(clickCoords[0], clickCoords[1])

                self.move(screen, row, col)
                self.win = logic.checkWin(self.grid)
                self.tie = logic.checkTie(self.grid)

        self.endGame(screen)
        
        pygame.display.flip() # call it only once to avoid flickering

        return None