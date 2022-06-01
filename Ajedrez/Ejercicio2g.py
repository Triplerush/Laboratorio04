from interpreter import draw
from chessPictures import *

#Piezas
piecesWhite = rock.join(knight).join(bishop)
piecesWhite = piecesWhite.join(queen).join(king).join(piecesWhite)
piecesBlack = piecesWhite.negative()
piecesWhite = piecesWhite.up(pawn.horizontalRepeat(8))
piecesBlack = pawn.horizontalRepeat(8).negative().up(piecesBlack)

#Tablero
picture = square.join(square.negative())
picture = picture.horizontalRepeat(4)
picture = picture.negative().up(picture)

whiteSelf = picture.under(piecesWhite)
blackSelf = picture.under(piecesBlack)
center = picture.verticalRepeat(2)

tablero = whiteSelf.up(center).up(blackSelf)

draw(tablero)