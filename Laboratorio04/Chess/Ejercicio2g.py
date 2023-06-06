from interpreter import draw
from chessPictures import *
#CASILLAS
# casillaBN = casilla blanca y negra, uno al lado de otra
casillaBN = square.join(square.negative())
# fila = se repite casillaBN 4 veces
fila = casillaBN.horizontalRepeat(3)
# fila2 = se duplica fila debajo de otra pero con los colores cambiados
# AHI SE PONDRAN LAS PIEZAS
fila2 = fila.up(fila.negative())
campoBatalla = fila2.verticalRepeat(1)
# PIEZAS
# tca = Torre, Caballo, Alfil. Por defecto son blancos, contrario a act
tca = rock.join(knight).join(bishop)
act = tca.verticalMirror()
# retaguardia = tca + reina + rey + tcaI
retaguardia = tca.join(queen).join(king).join(act)
#frente = peones
frente = pawn.horizontalRepeat(7)
# equipo = retaguardia + frente
equipoNegro = frente.up(retaguardia).negative()
equipoBlanco = retaguardia.up(frente)

ubicacionNegro = fila2.under(equipoNegro)
ubicacionBlanco = fila2.under(equipoBlanco)
tablero = ubicacionNegro.up(campoBatalla).up(ubicacionBlanco)
draw(tablero)