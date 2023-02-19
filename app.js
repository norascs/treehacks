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

  app.listen(port, () => {
    console.log(`Example app listening on port ${port}`)
  })