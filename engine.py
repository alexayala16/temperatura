"""
Éste archivo se encargará de cargar conlos datos,llevar cuenta de los movimientos válidos,asi como permirtilos.
"""

class gameState ():
    def _init_(self):
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--","--", "--",],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"],
            ] 
            self.moveFunctions = {'P': self.getPawnMoves, 'R': self.getPawnMoves,'N': self.getPawnMoves,'B': self.getPawnMoves,'Q': self.getPawnMoves, 'K': self.getPawnMoves,}
            self.whiteToMove = True
            self.moveLog = []
            self.whiteKingLocation = (7, 4)
            self.blackKingLocation = (0, 4)
            self.inCheck = []
            self.pins = []
            self.checks = []
            self.checkMate = False
            self.staleMate = False
            self.enPassantPossible = ()
            #
            self.wCastlekingside = True
            self.wCastleQueenside = True
            self.bCastlekingside = True
            self.bCastleQeenside = True
            self.castleRightsLog = [CastleRights(self.wCastleKingside, self.bCastleKingside, self.wCastleQueenside, self.bCastleQueenside)]
        
    """
    Permite hecer los movimientos que son ya porcesados en la clese Move (No sirve para los movimientos especiales como el enroque, las promociones de peones o las capturas de los pasos de los mismos).
    """
    def makeMove(self, move):
        self.board[move.StartRow][move.startCol]="--"
        self.board[move.endRow][move.endCol] = move.pieceMoved
        self.moveLog.append(move)#
        self.whiteTomove = not self.whiteToMove #
        #
        if move.pieceMoved =='Wk':
            self.whiteKingLocation = (move.endRow, move.endCol)
        elif move.pieceMved == 'bk':
            self.blackkingLocation = (move.endRow, move.endCol)
        #
        if move.pieceMoved[1] = 'p' and abs(move.startRow - move.endRow) == 2:
           self.enPassantPossible =((move.endRow + move.startRow) // 2, move.endCol)
        else:
            self.enPassantPossible = ()
        #
        if move.enPassant:
            self.board[move.startRow][move.endCol] = '--'
        #
        if move.pawnPromotion == True:
            promotedPiece = input('\nPromosión del peón a:\nReina (Q), Alfil (B), Caballo (N) o Terre (R).\nIgresa la letra que está entre parentesis pero en minúscula.\nElijo: ')
            if (promotedPiece == 'q') or (promotedPiece == 'b') or (promotedPiece == 'n') or (promotedPiece =='r'):
                self.board[move.endRow][move.endCol] = move.pieceMoved[0] + promotedPiece.upper()
            else:
                error = True
                while (error == True):
                    print('\nCódigo erroneo.')
                    promotedPiece = input('Promosión del peoń a:\Reina (Q), Alfil (B), Caballo (N) o Torre (R).\nIngresa la letra que está entre parentesis pero en minúnuscula.\nEljo: ')
                    if (promotedPiece == 'q') or (promotedPiece == 'b' or (promotedPiece == 'n') or (promotedPiece == 'r'):
                        self.board[move.endRow][moe.endCol] = move.pieceMove[0] + promotedPiece.upper()
                        error = False
        #
        self.updateCastleRights(move)
        self.castleRightslog.apeend(castleRights(self.wCastleKingside, self.wCastelQueenside, selfbCastleKingside, self.bCastleQueenssid))
        #
        if move.castle:
            if move.endCol - move.startCol == 2:
                self.board[move.endRow][move.endCol - 1] = self.board[move.endRow][move.endCol + 1]
                self.board[move.endRow][move.endCol + 1] = '--'
            else:
                self.board[move.endRow][move.endCol + 1] = self.board[move.endRow][move.endCol - 2]
                self.board[move.endRow][move.endCol - 2] = '--'

    """
    Permite regresar un movimiento.
    """
    def undoMove(self):
        if len(self.moveLog) != 0:
            move = self.moveLog.pop()
            self.board[move.startRow][move.startCol] = move.pieceMoved
            self.board[move.endRow][move.endCol] = move.pieceCaptured
            self.whiteToMove = not self.whiteToMove
            #
            if move:pieceMoved == 'wk':
                self.whitekingLocation = (move.startRow, move.startCol)
            elif move.pieceMoved = 'bk':
                self.blackkingLocation = (move.startRow, move.startCol)
            #
            if move.enPassant:
                self.board[move.endRow][move.endCol] = '--'
                self.board[move.startRow][move.endCol] = move.pieceCaptured
                self.enPassantPossible = (move.endRow, move.endCol)
            #
            if move.pieceMoved[1] == 'P' and abs(move.starRow - move.endRow) == 2:
                self.enPassantPossible = ()

            #
            self.castleRightsLog.pop()
            castleRights = self.castleRightsLog[-1]
            self.wCastleKingside = castleRights.wks
            self.wCastleQueenside = castleRights.wqs
            self.bCastleKingSide = castleRights.bks
            self.bCastleQueenSide = castleRights.bqs

            #
            if move.castle:
                if move.endCol - move.startColl == 2:
                    self.board[move.endRow][move.endCol + 1] = self.board[move.endRow][move.ensCol - 1]
                    self.board[move.endRow][move.endCol - 1] = '--'
                else:
                    self.board[move.endRow][move.endCol - 2] = self.board[move.endRow][move.endCol + 1]
                    self.board[move.endRow][move.endCol + 1] = '--'
            
            self.checkMate = False
            self.staleMate = False
    
    """
    Chequeo de los movimientos considerando los jaques.
    """
    def getValidMoves(self):
        moves = []
        self.inCheck,self.pins, self.checks = self.checkForPinsAndChecks()
        if self.whiteToMove:
             kingRow = self.whiteKingLocation[0]
            kingCol = self.whiteKingLocation[1]
        else:
            KingRow = self.blackkingLocation[0]
            KingCol = self.blackkingLocation[1]
        if self.inCheck:
            if len(self.checks) == 1:
                moves = self.gatAllPossibleMoves()
                #
                check = self.checks[0]
                checkCol = checks[0]
                checkCol = check[1]
                pieceChecking = self.board[checkRow][checkCol]
                validSquares = []
                #
                if pieceChecKing[1] == 'N':
                    validSquares = [(checkRow, checkCol)]
                else:
                    for i in range(1, 8):
                        validSquare = (kingRow + check[2] * i, kingCol + check[3] * i)
                        validSquares.append(validSquare)
                        if validSquare[0] == checkRow and validSquare[1] == checkCol:
                            break
                #
                for i in range(len(moves)-1, -1, -1):
                    if moves[i].pieceMoved[1] !='k':
                        if not (moves[i].endRow, moves[i].endCol) in validSquares:
                            moves.remove(movs[i])
            else:
                self.getkingMoves(kingRow,kingCol, moves)
        else:
            moves = self.getAllpossibleMoves()
        if len(moves) == 0:
            if self.incheck:
                self.checkMate = True
            else:
                self.staleMate = True
        else:
            self.checkMate = False
            self.staleMate = False
        return moves
    
    def checkForPinsAndChecks(self):
        pins = []
        checks = []
        inCheck = False
        if self.whileToMove:
            enemyColor = "b"
            allyColor = "w"
            startRow = self.whiteKingLocation[0]
            startCol = self.whiteKingLocation[1]
        else:
            enemyColor = "w"
            allyColor = "b"
            startRow = self.blackkingLocation[0]
            startCol = self.blackkingLocation[1]
        
        #Estoy en la linea 188 minuto 24:13