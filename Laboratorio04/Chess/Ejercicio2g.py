from interpreter import draw
from chessPictures import *
casillaBN = square.join(square.negative())
fila = casillaBN.horizontalRepeat(3)
fila2 = fila.up(fila.negative())
tablero = fila2.verticalRepeat(3)
draw(tablero)