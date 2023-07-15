<div align="center">
<table>
    <theader>
        <tr>
            <td><img src="https://github.com/rescobedoq/pw2/blob/main/epis.png?raw=true" style="width:50%; height:auto"/></td>
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
<tr><td>TÍTULO DE LA PRÁCTICA:</td><td colspan="5">Django Relaciones Uno a muchos y Muchos a muchos en BD</td></tr>
<tr>
<td>NÚMERO DE PRÁCTICA:</td><td>07</td><td>AÑO LECTIVO:</td><td>2023 A</td><td>NRO. SEMESTRE:</td><td>III</td>
</tr>
<tr>
<td>FECHA INICIO:</td><td>07-07-2023</td><td>FECHA FIN:</td><td>14-07-2023</td><td>DURACIÓN:</td><td>04 horas</td>
</tr>
<tr><td colspan="6">INTEGRANTES:
    <ul>
        <li>Forocca Mamani Maxs Sebastian Joaquin</li>
    </ul>
</td>
</<tr>
<tr><td colspan="6">DOCENTE:
<ul>
<li>Anibal Sardon</li>
</ul>
</td>
</<tr>
</tdbody>
</table>


#


## EJERCICIOS PROPUESTOS

  - Relación de uno a muchos
    - Código: Para realizar la relación de uno a muchos en bases de datos de Django, se inspeccionaron los videos del Laboratorio y se creo una version similar en el archivo models.py de la aplicacion: "Aplicacion1", del proyecto: "Proyecto", del presente trabajo. Donde se tiene a la Clase Lenguaje y Framework, en la cual los frameworks tienen un lenguaje con el que trabajan y los lenguajes pueden tener varios frameworks, se utiliza "models.Foreignkey()" para hacer la relación de uno a muchos.
    - ![Codigo_OtM](1-OtM_codigo.png)
    - Agregar y Consultas: Para agregar y consultar en la DB, se hizo las respectivas migraciones y se abrio un shell donde se importa las clases de Lenguaje y Framework. Posterior a ello se crean objetos de las clases importadas, se guardan en la base de datos y se relacionan a los frameworks con sus respectivos lenguajes. Para realizar consultas, se utiliza "objects.filter" para Lenguaje y Framework especificandose el nombre o inicio de nombre en los parametros para hacer el filtrado y obtener la información solicitada.
    - ![AgregaryConsultas_OtM](1-OtM_Query.png)
    - Tabla de Lenguajes: En la siguiente imagen se muestra la tabla de Lenguajes despues de agregar la información a la base de datos en el shell, para ello se utilizo DB Browser for SQLite.
    - ![TablaLenguaje_OtM](1-OtM_lenguaje.png)
    - Tabla de Frameworks: En la siguiente imagen se muestra la tabla de Framewoks despues de agregar la información a la base de datos en el shell, para ello se utilizo DB Browser for SQLite. Y se puede evidenciar la relación de uno a muchos en la columna "lenguaje_id".
    - ![TablaFramework_OtM](1-OtM_framework.png)


  - Relación muchos a muchos
    - Código: Para realizar la relación de muchos a muchos en bases de datos de Django, se inspeccionaron los videos del Laboratorio y se creo una version similar. Donde se tiene a la Clase Movie (pelicula) y Character (personaje), en la cual las peliculas pueden tener varios personajes y los personajes pueden pertenecer a varias peliculas, se utiliza "models.ManyToManyField()" para hacer la relacion de muchos a muchos.
    - ![Codigo_MtM](2-MtM_codigo.png)
    - Agregar y Consultas: Para agregar y consultar en la DB, se hizo las respectivas migraciones y se abrio un shell donde se importa las clases de Movie y Character. Posterior a ello se crean objetos de las clases importadas, se guardan en la base de datos con ".save()" y se relacionan a los Character con sus respectivas Movie utilizando ".add()" o creandolo directamente con ".create()". Para realizar consultas, se utiliza "objects.filter" para Movie y Character especificandose el nombre en los parametros para hacer el filtrado y obtener la información solicitada.
    - ![AgregaryConsultas_MtM](2-MtM_Query.png)
    - Tabla de Movie: En la siguiente imagen se muestra la tabla de Movie despues de agregar la información a la base de datos en el shell, para ello se utilizo DB Browser for SQLite.
    - ![TablaMovie_MtM](2-MtM_movie.png)
    - Tabla de Character: En la siguiente imagen se muestra la tabla de Character despues de agregar la información a la base de datos en el shell, para ello se utilizo DB Browser for SQLite.
    - ![TablaCharacterMtM](2-MtM_character.png)
    - Tabla de Movie_Character: En la siguiente imagen se puede evidenciar la relacion de muchos a muchos de Movie y Character, para ello se tiene las columnas de "movie_id" y "character_id". Esta tabla se crea automaticamente despues de migrar con la relacion Many To Many.
    - ![TablaMovieCharacter](2-MtM_movie_character.png)

      
  - Impresión de pdfs 
  - Envio de emails
  - Commits
#

## CUESTIONARIO


#

## REFERENCIAS

#
