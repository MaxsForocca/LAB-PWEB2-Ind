from interpreter import draw
from chessPictures import *
caballoB = knight
caballoN = knight.negative()
rpta1 = caballoB.join(caballoN)
rpta2 = rpta1.up(rpta1.negative())
draw(rpta2)