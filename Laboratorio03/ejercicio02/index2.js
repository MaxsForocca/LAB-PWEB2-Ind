const path = require('path');
const express = require('express');
const app = express();

app.listen(3000, () => {
    console.log("Maxs esta escuchando en: http://localhost:3000")

});

app.get('/', (request, response) => {
    response.sendFile(path.resolve(__dirname, 'index.html'));
});