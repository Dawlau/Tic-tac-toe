class Singleplayer():
    
    def __init__(self):
        self.resetVars()


    def resetVars(self):

        from ai import AI

        self.player = 0
        self.renderEndGameMessage = False
        self.AI = AI()

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


    def endGame(self, screen):

        import graphics

        if (self.win or self.tie) and not self.renderEndGameMessage:

            self.renderEndGameMessage = True
            
            message = None

            if self.win:
                message = ("O" if self.player == 0 else "X") + " won!"
            else:
                message = "It's a tie!"

            graphics.renderMsgAboveGrid(screen, message)

    
    def playerMove(self, screen, row, col):

        import graphics

        if row == None:
            return
                
        if self.grid[row][col] != "#":
            return
        
        graphics.drawX(screen, self.grid, row, col)

        self.player ^= 1

    
    def aiMove(self, screen, row, col):

        import graphics

        graphics.drawO(screen, self.grid, row, col)

        self.player ^= 1


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
            elif (not self.win and not self.tie):
                if self.player == 0 and event.type == pygame.MOUSEBUTTONDOWN:

                    clickCoords = event.pos
                    row, col = logic.getCell(clickCoords[0], clickCoords[1])
                    self.playerMove(screen, row, col)
                    
                elif self.player == 1:
                    row, col = self.AI.getCell(self.grid)
                    self.aiMove(screen, row, col)

                self.win = logic.checkWin(self.grid)
                self.tie = logic.checkTie(self.grid)

        self.endGame(screen)
        
        pygame.display.flip() # call it only once to avoid flickering

        return None