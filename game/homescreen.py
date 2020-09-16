class HomeScreen:

    def __init__(self):
        self.spCoords = None
        self.spHeight = None
        self.spWidth = None
        self.mpCoords = None
        self.mpHeight = None
        self.mpWidth = None


    def renderSingleplayer(self, screen):
        
        from graphics import TMR30
        import constants

        spText = "Singleplayer"
        spWidth, spHeight = TMR30.size(spText)
        spCoords = [self.mpCoords[0], self.mpCoords[1] - spHeight]

        text = TMR30.render(spText, True, constants.black)
        screen.blit(text, spCoords)

        self.spCoords = spCoords
        self.spWidth = spWidth
        self.spHeight = spHeight


    def renderMultiplayer(self, screen):

        from graphics import TMR30
        import constants

        mpText = "Multiplayer"
        mpWidth, mpHeight = TMR30.size(mpText)
        mpCoords = [constants.width // 2 - mpWidth // 2, constants.height // 2 - mpHeight // 2]

        text = TMR30.render(mpText, True, constants.black)
        screen.blit(text, mpCoords)

        self.mpCoords = mpCoords
        self.mpHeight = mpHeight
        self.mpWidth = mpWidth



    def render(self, screen):

        import constants
        import pygame

        screen.fill(constants.white)

        self.renderMultiplayer(screen)
        self.renderSingleplayer(screen)

        pygame.display.flip()

    
    def getOption(self):

        import pygame

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:

                clickCoords = event.pos
     
                if self.spCoords[0] <= clickCoords[0] <= self.spCoords[0] + self.spWidth and self.spCoords[1] <= clickCoords[1] <= self.spCoords[1] + self.spHeight:
                    return "SP"

                if self.mpCoords[0] <= clickCoords[0] <= self.mpCoords[0] + self.mpWidth and self.mpCoords[1] <= clickCoords[1] <= self.mpCoords[1] + self.mpHeight:
                    return "MP"