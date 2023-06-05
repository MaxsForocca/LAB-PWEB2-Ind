from colors import *
class Picture:
    def __init__(self, img):
        self.img = img;

    def __eq__(self, other):
        return self.img == other.img

    def _invColor(self, color):
        if color not in inverter:
            return color
        return inverter[color]

    def verticalMirror(self):
        """ Devuelve el espejo vertical de la imagen """
        # RETORNA UN ARRAY (IMG)
        vertical = []
        for value in self.img:
            vertical.append(value[::-1])
        return vertical

    def horizontalMirror(self):
        """ Devuelve el espejo horizontal de la imagen """
        # retorna un array IMG
        horizontal = self.img[::-1]
        return horizontal

    def negative(self):
        """ Devuelve un negativo de la imagen """
        # Retorna un array IMG
        nega = []
        for value in self.img:
            str = ''
            for i in value:
                str += self._invColor(i)
            nega.append(str)
        negativo = Picture(nega)
        return negativo

    def join(self, p):
        """ Devuelve una nueva figura poniendo la figura del argumento 
            al lado derecho de la figura actual """
        rpta = Picture(self.img)
        for i in range(0, len(self.img)):
            rpta.img[i] = rpta.img[i] + p.img[i]
        return rpta

    def up(self, p):
        rpta = Picture(self.img)
        for i in range(0, len(self.img)):
            rpta.img.append(p.img[i])
        return rpta

    def under(self, p):
        """ Devuelve una nueva figura poniendo la figura p sobre la
            figura actual """
        rpta = []
        for value in p.img:
            rpta.append(value.replace(' ','='))
        return rpta
    
    def horizontalRepeat(self, n):
        """ Devuelve una nueva figura repitiendo la figura actual al costado
            la cantidad de veces que indique el valor de n """
        return Picture(None)

    def verticalRepeat(self, n):
        return Picture(None)

    #Extra: Sólo para realmente viciosos 
    def rotate(self):
        """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
        o antihorario"""
        return Picture(None)
