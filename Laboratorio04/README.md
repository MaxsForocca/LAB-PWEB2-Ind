<div align="center">
<table>
    <theader>
        <tr>
            <td><img src = "https://github.com/rescobedoq/pw2/blob/main/epis.png?raw=true" alt="EPIS" style="width:50%; height:auto"/></td>
            <th>
                <span style="font-weight:bold;">UNIVERSIDAD NACIONAL DE SAN AGUSTIN</span><br />
                <span style="font-weight:bold;">FACULTAD DE INGENIERÍA DE PRODUCCIÓN Y SERVICIOS</span><br />
                <span style="font-weight:bold;">DEPARTAMENTO ACADÉMICO DE INGENIERÍA DE SISTEMAS E INFORMÁTICA</span><br />
                <span style="font-weight:bold;">ESCUELA PROFESIONAL DE INGENIERÍA DE SISTEMAS</span>
            </th>
            <td><img src="https://github.com/rescobedoq/pw2/blob/main/abet.png?raw=true" alt="ABET" style="width:50%; height:auto"/></td>
        </tr>
    </theader>
    <tbody>
        <tr><td colspan="3"><span style="font-weight:bold;">Formato</span>: Práctica de Laboratorio</td></tr>
        <tr><td><span style="font-weight:bold;">Aprobación</span>:  2022/03/01</td><td><span style="font-weight:bold;">Código</span>: GUIA-PRLD-001</td><td><span style="font-weight:bold;">Página</span>: 1</td></tr>
    </tbody>
</table>
</div>

<div align="center">
<span style="font-weight:bold;">GUÍA DE LABORATORIO</span><br />
</div>


<table>
<theader>
<tr><th colspan="6">INFORMACIÓN BÁSICA</th></tr>
</theader>
<tbody>
<tr><td>ASIGNATURA:</td><td colspan="5">Programación Web 2</td></tr>
<tr><td>TÍTULO DE LA PRÁCTICA:</td><td colspan="5">Python</td></tr>
<tr>
<td>NÚMERO DE PRÁCTICA:</td><td>04</td><td>AÑO LECTIVO:</td><td>2023 A</td><td>NRO. SEMESTRE:</td><td>III</td>
</tr>
<tr>
<td>FECHA INICIO:</td><td>30-May-2022</td><td>FECHA FIN:</td><td>5-Jun-2022</td><td>DURACIÓN:</td><td>04 horas</td>
</tr>
<tr><td colspan="6">INTEGRANTES:
    <ul>
        <li>Forocca Mamani Maxs Sebastian Joaquin</li>
    </ul>
</td>
</<tr>
<tr><td colspan="6">DOCENTE:
<ul>
<li>Aníbal Sardón</li>
</ul>
</td>
</<tr>
</tdbody>
</table>


#


## EJERCICIOS PROPUESTOS
- En esta tarea usted pondrá en práctica sus conocimientos de programación en Python para dibujar un tablero de Ajedrez.

- La parte gráfica ya está programada, usted sólo tendrá que concentrarse en las estructuras de datos subyacentes.

- Con el código proporcionado usted dispondrá de varios objetos de tipo Picture para poder realizar su tarea:

- Estos objetos estarán disponibles importando la biblioteca: chessPictures y estarán internamente representados con arreglos de strings que podrá revisar en el archivo pieces.py

- La clase Picture tiene un sólo atributo: el arreglo de strings img, el cual contendrá la representación en caracteres de la figura que se desea dibujar.

- La clase Picture ya cuenta con una función implementada, no debe modificarla, pero si puede usarla para implementar sus otras funciones: 
  - _invColor: recibe un color como un caracter de texto y devuelve su color negativo, también como texto, deberá revisar el archivo colors.py para conocer los valores negativos de cada caracter.
- La clase Picture contará además con varios métodos que usted deberá implementar:
  - verticalMirror: Devuelve el espejo vertical de la imagen
    - En el metodo vericalMirror: Se crea un Picture 'rpta' y se una lista 'vertical' que agregara Strings con los caracteres cambiados de orden de 'self.img' usando 'vertical.append(self.img[::-1])' y se agrega a 'rpta' retornandose este ultimo.
  ![metodoVerticalMirror](imagenes/metodoVerticalMirror.png)
  - horizontalMirror: Devuelve el espejo horizontal de la imagen
    - En el metodo horizontalMirror: Se crea un lista 'horizontal' donde se agregaran los elementos de la lista 'self.img' pero en orden cambiado, el ultimo primero, y finalmente retorna la lista 'horizontal'.
  ![metodoHorizontalMirror](imagenes/metodoHorizontalMirror.png)
  - negative: Devuelve un negativo de la imagen
    - El metodo negative: Crea una lista 'nega' donde se iran añadiendo los elementos del 'self.img' pero con los caracteres cambiados a su inverter, se usan dos bucles for, el primero itera cada elemento de la lista 'self.img' y tambien crea un String vacio 'str'. El segundo bucle itera entre cada caracter del elemento del primer bucle y se agregan a 'str' los caracteres que devuelve la funcion _invColor. Despues 'str' se agrega a 'nega' que a su ves se manda como parametro a un nuevo Picture 'negativo', finalmente se retorna 'negativo'.
  ![metodoNegative](imagenes/metodoNegative.png)
  - join: Devuelve una nueva figura poniendo la figura del argumento al lado derecho de la figura actual
    - El metodo join: Crea un Picture 'rpta' con la lista de 'self' y se crea un bucle for que iterara entre el rango de 0 y la longitud de 'self.img', en el bucle se agregaran a cada String de 'rpta.img' los String de 'p.img' que es uno de los argumentos. Finalemnte se retorna 'rpta'.
  ![metodoJoin](imagenes/metodoJoin.png)
  - up: Devuelve una nueva figura poniendo la figura recibida como argumento, encima de la figura actual
    - El metodo up: Crea un Picture 'rpta' similar al del metodo join. Tambien crea un bucle for que itera entre 0 y la longitud de 'p.img', en el bucle se agragan los elementos de 'p.img' debajo de 'rpta.img' usando append. Finalmente se retorna 'rpta'.
  ![metodoUp](imagenes/metodoUp.png)
  - under: Devuelve una nueva figura poniendo la figura recibida como argumento, sobre la figura actual
    - El metodo under: 
  ![metodoUnder](imagenes/metodoUnder.png)
  - horizontalRepeat, Devuelve una nueva figura repitiendo la figura actual al costado la cantidad de veces que indique el valor de n
  ![metodoHorizontalRepeat](imagenes/metodoHorizontalRepeat.png)
  - verticalRepeat Devuelve una nueva figura repitiendo la figura actual debajo, la cantidad de veces que indique el valor de n
  ![metodoVerticalRepeat](imagenes/metodoVerticalRepeat.png)
- Tenga en cuenta que para implementar todos estos métodos, sólo deberá trabajar sobre la representación interna de un Picture, es decir su atributo img.

- Para dibujar una objeto Picture bastará importar el método draw de la biblioteca interpreter y usarlo de la siguiente manera:

$ python3
Python 3.9.2 (default, Feb 28 2021, 17:03:44) 
[GCC 10.2.1 20210110] on linux
Type "help", "copyright", "credits" or "license" for more information.

>>> from chessPictures import *
>>> from interpreter import draw
pygame 1.9.6
Hello from the pygame community. https://www.pygame.org/contribute.html
>>> draw(rock)

- Ejercicios:
  - Para resolver los siguientes ejercicios sólo está permitido usar ciclos, condicionales, definición de listas por comprensión, sublistas, map, join, (+), lambda, zip, append, pop, range.
  - Implemente los métodos de la clase Picture. Se recomienda que implemente la clase picture por etapas, probando realizar los dibujos que se muestran en la siguiente preguntas.
  - Usando únicamente los métodos de los objetos de la clase Picture dibuje las siguientes figuras (invoque a draw):
  - Ejercicio2a
    - Codigo
    ![codigoEjercicio2a](imagenes/codigoEjercicio2a.png)
    - Prueba a
    ![pruebaEjercicio2a](imagenes/pruebaEjercicio2a.png)
  - Ejercicio2b
    - Codigo
    ![codigoEjercicio2b](imagenes/codigoEjercicio2b.png)
    - Prueba b
    ![pruebaEjercicio2b](imagenes/pruebaEjercicio2b.png)
  - Ejercicio2c
    - Codigo
    ![codigoEjercicio2c](imagenes/codigoEjercicio2c.png)
    - Prueba c
    ![pruebaEjercicio2c](imagenes/pruebaEjercicio2c.png)
  - Ejercicio2d
    - Codigo
    ![codigoEjercicio2d](imagenes/codigoEjercicio2d.png)
    - Prueba d
    ![pruebaEjercicio2d](imagenes/pruebaEjercicio2d.png)
  - Ejercicio2e
    - Codigo
    ![codigoEjercicio2e](imagenes/codigoEjercicio2e.png)
    - Prueba e
    ![pruebaEjercicio2e](imagenes/pruebaEjercicio2e.png)
  - Ejercicio2f
    - Codigo
    ![codigoEjercicio2f](imagenes/codigoEjercicio2f.png)
    - Prueba f
    ![pruebaEjercicio2f](imagenes/pruebaEjercicio2f.png)
  - Ejercicio2g
    - Codigo
    ![codigoEjercicio2g](imagenes/codigoEjercicio2g.png)
    - Prueba g
    ![pruebaEjercicio2g](imagenes/pruebaEjercicio2g.png)
#

## CUESTIONARIO
- ¿Qué son los archivos *.pyc?
  - R
- ¿Para qué sirve el directorio pycache?
  - R
- ¿Cuáles son los usos y lo que representa el subguión en Python?
  - R
#

## REFERENCIAS
https://www.aluracursos.com/blog/append-o-extend-agregar-elementos-a-la-lista-con-python 
#
