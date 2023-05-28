const fs = require('fs');
const path = require('path');
const express = require('express');
const app = express();
// USAR PUB, ESTATICO
app.use(express.static('pub'));
// ESCUCHAR
app.listen(3000, () => { //el puerto puede se cambiado
    console.log('Se esta escuchando desde: http://localhost:3000') // si el puerto cambia, tambien el link
});
// SOLICITAR EL ARCHIVO QUE SE ABRIRA (enviar) ; RAIZ
app.get('/', (request, response) => {
    response.sendFile(path.resolve(__dirname, 'index.html'));
});
// EN EL LINK linkNormal/recitar; (leer) el archivo.txt
app.get('/recitar', (request, response) => {
    fs.readFile(path.resolve(__dirname, 'priv/poema.txt'), 'utf8',
    (err, data) => {
        if(err) {
            console.log(err)
            response.status(500).json({
                error : 'message'
            });
            return
        }
        response.json({
            text : data.replace(/\n/g, '<br>') // cambiar saltos de linea por <br> 
        });
    });
});