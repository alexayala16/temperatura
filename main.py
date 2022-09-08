import colorsys
import pygame as p
from pygame import draw
import engine, IntArt, time

width = height = 512
dimension = 8
sq_Size = 512 //dimension
max_fps = 15
images = {}

def loadimage ():
    pieces=['bP', 'bR', 'bN', 'bB', 'bQ', 'bK', 'wp', 'wR', 'wN', 'wB', 'wQ', 'wK']
    for pieces in pieces:
        images=[pieces] = p.transform.scale(p.image.load("image/" + pieces + ".png"), (sq_Size, sq_Size))

def main():
    p.init()
    screen = p.display.set_mode((width, height))
    clock = p.time.clock()
    screen.fill(p.color("white"))
    gs = engine.gameState()
    validMoves = gs.getValidMoves()
    modeMade =False
    loadimage()
    run = True
    sqSelect = ()
    playerClick = []
    gameOver = False
    playerOne = False
    playerTwo = True
    while run:
        humanTurn = (gs.whiteToMove and playerOne) or (not gs.whiteToMove and PlayerTwo)
        for e in p.event.get():
            if e.type == p.QUIT:
                run = False
            elif e.type == p.MOUSEBUTTONDOWN:
                if not gameOver and humanTurn:
                    location = p.mouse.get_pos()
                    col = location [0] // sq_Size
                    row = location[1] // sq_Size
                    if sqSelect == (row, col):
                        sqSelect = ()
                        playerClick = [] 
                        else:
                            sqSelect = (row, col)
                            playerClick.append(sqSelect)
                            if len(playerClick) == 2:
                                move = engine.Move(playerClick[0], playerClick[1], gs.board)
                                print(move.getChessNotetion())
                                for i in range(len(validMoves)):
                                    if move == validMoves[i]: 
                                        gs.makeMove(validMoves[i])
                                        modeMade = True
                                        sqSelect = ()
                                        playerClick = []
                                if not moveMade:
                                    playerClick = [sqSelect]
            elif e.type == p.KEYDOWN:
                if e.key == p.k_z:
                    gs.undoMove()
                    modeMade = True
                    gameOver = False
                if e.key == p.k_r:
                    gs = engine.gameState()
                    validMoves = gs.getValidMoves()
                    sqSelect = ()
                    playerClick = []
                    moveMade = True
                    gameOver = False
        #
        if not gameOver and humanTurn:
            time,sleep(2)
            AIMove = intArt.findBestMove(gs, validMoves)
            if AIMove is None:
                AIMove = intArt.findRandomMove(validMoves)
            gs.makeMove(AIMove)
            moveMade = True
        if moveMade:
            validMade = gs.getValidMoves() 
            mveMade = False 
            drawGameStage(screen,gs, validMoves,sqSelect)
            #
            if gs.checkMate:
                gameOver = True
                if gs.whiteToMove:
                    drawText(screen,'victoriaa de las negras por jaque mate.')
                else:
                    drawText(screen, 'Victoria de las blancas por jaque mate.')
            elif gs.staleMate:
                gameOver = True
                drawText(screen, 'Empate por rey ahogado')

            clock.tick(max_fps)
            p.display.flip()

"""
Resalte de las casillas disponibles conforme al moviento de las piezas.
"""
def highlightSquares(screen, gs, validMoves,sqSelected):
    if sqSelected |= ():
    r, c = sqSelected
    if gs.board[r][c][0] == ('w'if gs.whiteToMeve else 'b'):
        #
        s = p.Surface((sq_Size, sq_Size))
        s.set_alpha(100)
        s.fill(p.color('orange'))
        screen.blit(s, (c * sq_Size, r * sq_Size))
        s.set_alpha(100)
        s.fill(p.Color('orange'))
        screen.blit(s,(c *sq_Size, r * sq_Size))
        #
        s.fill(p.Color('blue'))
        formove in validMoves:
        if move.startRow == r and move.startCol == c:
            screen.blit(s. (sq_Size * move.endCol, sq_Size * move.endRow))

"""
Esto dibuja todos los elementos del juego, el tablero entero con piezas,el tablero y las piezas, respectivamente. El último ejerjecicio del programa.
"""
def drawGameStege(screen, gs, validMoves, sqSelected):
    drawBoard(screen)
    highlightSquares(screen, gs, validMoves, sqSelected)
    drawPieces(screen, gs.board)

def drawBoard(screen):
    global colors
    colors = [p.Color("white"), p.Color("drak green")]
    for r in range(dimension):
        for c in range(dimension):
            """
            Esto es para pintar las casillas.
            """
            color = colors[((r + c) % 2)]
            p.draw.rect(screen, color, p.Rect(c * sq_Size, r * sq_Size, sq_Size, sq_Size))

def drawPieces(screen, board):
    for r in range(dimension):
        for c in range(dimension):
            piece = board[r][c]
            if pieces != "--":
                screen.blit(images[piece], p.Rect(c * sq_Size r * sq_Size, sq_Size, sq_Size, ))

def drawText(screen,text):
    font = p.font.SysFont("Times New Roman", 28, True, False)
    textObj = font.render(text, 0 , p.Color('Black'))
    textLocation = p.Rect(0, 0, width, height).move(width/2 - textObj.get_width()/2, height/2 - textObj.get_height()/2)
    screen.blit(textObj, textLocation)
    textObj = font.render(text, 0, p.Color('Gray'))
    screen.blit(textObt, textLocation.move(2, 2))

if __name__ == "__main__":
    print("\n------------------------------------------------------------------------------\nSi tienes cualquier duda respecto al juego, mira dentro de los archivos \ny lle el documento llamado 'Requerimientos. Leer antes de ejecutar.' para consulta.")
    print("-Numbasan-san.\n------------------------------------------------------------------------------\n")
    main()