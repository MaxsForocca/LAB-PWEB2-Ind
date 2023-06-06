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
        # RETORNA UN Picture
        rpta = Picture(self.img)
        vertical = []
        for value in self.img:
            vertical.append(value[::-1])
        rpta.img = vertical
        return rpta

    def horizontalMirror(self):
        """ Devuelve el espejo horizontal de la imagen """
        # retorna un array img
        horizontal = self.img[::-1]
        return horizontal

    def negative(self):
        """ Devuelve un negativo de la imagen """
        # Retorna un Picture, se crea nega que servira para crear negativo
        nega = []
        for value in self.img:
            str = ''
            # el nuevo string se creara con los caracteres cambiados, se usa _invColor
            for i in value:
                str += self._invColor(i)
            nega.append(str)
        negativo = Picture(nega)
        return negativo

    def join(self, p):
        """ Devuelve una nueva figura poniendo la figura del argumento 
            al lado derecho de la figura actual """
        #retorna un Picture
        rpta = Picture(self.img)
        for i in range(0, len(self.img)):
            # el string de rpta se agrandara o tendra mas caracteres de p, graficamente a la derecha
            rpta.img[i] += p.img[i]
        return rpta

    def up(self, p):
        #retorna un Picture, self encima de p
        rpta = Picture(self.img)
        for i in range(0, len(p.img)):
            # se colocan los Strings de p, en orden despues de self
            rpta.img.append(p.img[i])
        return rpta

    def under(self, p):
        """ Devuelve una nueva figura poniendo la figura p sobre la
            figura actual """
        # se crea un arreglo vacio que se agregara a la figura que se retorne
        arrayCombinado = []
        # se itera simultaneamente los String de cada arreglo con zip 
        for cadena1, cadena2 in zip(self.img, p.img):
            str = ""
            # se itera los caracteres de cada String con zip
            for char1, char2 in zip(cadena1, cadena2):
                # no se considera al ' ' por que es el azul, sino se cambia los strings
                if char2 == ' ':   
                    str += char1             
                    continue
                str += char2
            # se agrega la nueva cadena al array
            arrayCombinado.append(str)
        rpta = Picture(arrayCombinado)
        return rpta
    
    def horizontalRepeat(self, n):
        """ Devuelve una nueva figura repitiendo la figura actual al costado
            la cantidad de veces que indique el valor de n """
        rpta = Picture(self.img)
        for i in range(0, len(self.img)):
            # se agragaran mas caracteres si n es almenos mayor a 0, se aumenta n veces rpta.img,
            # se vuelve a repetir la cadena n veces si es necesario
            rpta.img[i] = rpta.img[i] + (rpta.img[i]*n)
        return rpta

    def verticalRepeat(self, n):
        # se hace uso de extend que puede agragar los valores de varias listas en otra, parecido a append
        rpta = Picture(self.img)
        rpta.img.extend(rpta.img*n)
        return rpta

    #Extra: Sólo para realmente viciosos 
    def rotate(self):
        """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
        o antihorario"""
        return Picture(None)
