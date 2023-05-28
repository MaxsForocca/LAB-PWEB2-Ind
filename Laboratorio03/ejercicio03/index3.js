const path = require('path');
const express = require('express');
const app = express();
app.use(express.static('pub'));
app.listen(3000, () => {
    console.log('Se esta escuchando desde: http://localhost:3000')
});
app.get('/', (request, response) => {
    response.sendFile(path.resolve(__dirname,'index.html')); //tambien funciona con: response.sendFile(path.resolve('index.html'));
});
