const http = require('http');
const express = require('express');

var fs = require('fs');
const {resolve} = require('path');
const path = require('path')
const hostname = '127.0.0.1';
const port = 3000;
const app = express()




app.use(express.static(path.join(__dirname, 'public')))

app.get('/', (req, res) => {
    res.sendFile(resolve('index.html'))
  })
app.get('/', function(req, res) {
    request('http://127.0.0.1:5000/flask', function (error, response, body) {
        console.error('error:', error); 
        console.log('statusCode:', response && response.statusCode); 
        console.log('body:', body);
        res.send(body); 
      });      
});

  app.listen(port, () => {
    console.log(`Example app listening on port ${port}`)
  })