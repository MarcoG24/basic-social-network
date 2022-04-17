require('dotenv').config();
const express = require('express')
const app = express()
const port = process.env.PORT || 4000

const mysql = require('mysql2')
const connection = mysql.createConnection(DATABASE_URL=process.env.DATABASE_URL);

const path = require('path')

connection.connect()

let renderHTML = path.resolve(__dirname, './index.html');

app.get('/get-data', (req, res) => {
  console.log('************')
  console.log(req.query)
  console.log('************')
  const dataMock = [
    {
      email: 'prueba',
      password: 'prueba',
      type_user: 'admin',
      name: 'prueba'
    }
  ]
  console.log(dataMock)
  console.log('************')
  res.send(dataMock)
  // const query = 'SELECT * FROM users WHERE email= "' + req.query.email + '"'
  // connection.query(query, function (err, rows, fields) {
  //   if (err) res.send([])

  //   res.send(rows)
  //   console.log(rows)
  // })
})

app.get('/register-user', (req, res) => {
  console.log('************')
  console.log(req.query)
  console.log('************')
  const dataMock = '1'
  console.log(dataMock)
  console.log('************')
  res.send(dataMock)

  // let values= '('
  // let data= '('
  // Object.entries(req.query).forEach(entry => {
  //   const [key, value] = entry;
  //   data = data + key + ','
  //   values = values + '"' + value + '",'
  // });
  // const data_query = data.substring(0, data.length - 1) + ')'
  // const values_query = values.substring(0, values.length - 1) + ')'
  
  // const query = 'INSERT INTO users ' + data_query + ' VALUES ' + values_query
  // connection.query(query, function (err, rows, fields) {
  //   if (err) res.status(400).send('0')
  //   res.status(200).send(rows.affectedRows.toString())
    
  // })
})

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})

app.get('/', (req, res) => {
    console.log('hola')
    res.sendFile(renderHTML)
})