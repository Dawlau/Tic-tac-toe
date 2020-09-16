class AI:

    def __init__(self):
        
        self.scores = {"O" : 1,
                       "X" : -1,
                       "tie" : 0}


    def minimax(self, grid, player, alpha = -1000, beta = 1000, depth = 0): # "O maximizez and X minimezez"

        # player == 1 => "O"
        # player == 0 => "X"

        import logic

        if logic.checkWin(grid):
            if player == 0: # last move was made by 1 aka "O"
                return self.scores["O"]
            else:
                return self.scores["X"]
        
        if logic.checkTie(grid):
            return self.scores["tie"]

        bestScore = None
        r = None
        c = None
        tobreak = False

        for row in range(3):
            for col in range(3):
                if grid[row][col] == "#":
                    
                    if player == 0:
                        grid[row][col] = "X"
                    else:
                        grid[row][col] = "O"

                    score = self.minimax(grid, player ^ 1, alpha, beta, depth + 1)

                    if bestScore is None:
                        bestScore = score
                        r = row
                        c = col
                    else:
                        if player == 0:
                            if score < bestScore:
                                bestScore = score
                                r = row
                                c = col
                            beta = min(beta, score)
                        else:
                            if score > bestScore:
                                bestScore = score
                                r = row
                                c = col
                            alpha = max(alpha, score)

                    grid[row][col] = "#"

                    if beta <= alpha:
                        tobreak = True
                        break
            
            if tobreak:
                break


        if depth == 0:
            return r, c
        else:
            return bestScore

    def getCell(self, grid):

        # call minimax algorithm (is using alpha-beta pruning)
        return self.minimax(grid, 1)