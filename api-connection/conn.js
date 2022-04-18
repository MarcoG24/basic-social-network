require('dotenv').config();
const express = require('express')
const app = express()
const port = process.env.PORT || 4000

const mysql = require('mysql2')
const connection = mysql.createConnection(DATABASE_URL=process.env.DATABASE_URL);

const path = require('path')

connection.connect()

let renderHTML = path.resolve(__dirname, './index.html');

app.get('/get-user', (req, res) => {
  const query = 'SELECT * FROM users WHERE email= "' + req.query.email + '" AND password= "' + req.query.password + '"'
  console.log(query)
  connection.query(query, function (err, rows, fields) {
    if (err) res.send([])

    res.send(rows)
  })
})

app.get('/find-user', (req, res) => {

  const query = 'SELECT * FROM users WHERE email= "' + req.query.email + '"'
  connection.query(query, function (err, rows, fields) {
    if (err) res.send([])

    res.send(rows)
  })
})

app.get('/register-user', (req, res) => {
  let values= '('
  let data= '('
  Object.entries(req.query).forEach(entry => {
    const [key, value] = entry;
    data = data + key + ','
    values = values + '"' + value + '",'
  });
  const data_query = data.substring(0, data.length - 1) + ')'
  const values_query = values.substring(0, values.length - 1) + ')'
  
  const query = 'INSERT INTO users ' + data_query + ' VALUES ' + values_query
  connection.query(query, function (err, rows, fields) {
    if (err) res.status(400).send('0')
    res.status(200).send(rows.affectedRows.toString())
    
  })
})

app.get('/update-data-user', (req, res) => {

  let create_query = ''
  let data_where = ''
  Object.entries(req.query).forEach(entry => {
    const [key, value] = entry;
    const column = key + '= "' + value + '",'
    if (key === 'email') {
      data_where = column.substring(0, column.length - 1)
    } else {
      create_query = create_query + column
    }
  });
  const data_query = create_query.substring(0, create_query.length - 1) 
  
  const query = 'UPDATE users SET ' + data_query + ' WHERE ' + data_where
  connection.query(query, function (err, rows, fields) {
    if (err) res.status(400).send('0')
    res.status(200).send(rows.affectedRows.toString())
  })

})

app.get('/delete-data-user', (req, res) => {

  let data_where =  'email = "' + req.query['email'] + '"'
  
  const query = 'DELETE FROM users WHERE ' + data_where
  connection.query(query, function (err, rows, fields) {
    if (err) res.status(400).send('0')
    res.status(200).send(rows.affectedRows.toString())
  })

})

app.get('/get-posts', (req, res) => {
  const query = 'SELECT * FROM user_post'
  console.log(query)
  connection.query(query, function (err, rows, fields) {
    if (err) res.status(400).send('0')
    res.status(200).send(rows)
  })

})

app.get('/find-post', (req, res) => {

  const query = 'SELECT * FROM user_post WHERE id= "' + req.query.id + '"'
  connection.query(query, function (err, rows, fields) {
    if (err) res.send([])

    res.send(rows)
  })
})

app.get('/create-post', (req, res) => {
  let values= '('
  let data= '('
  Object.entries(req.query).forEach(entry => {
    const [key, value] = entry;
    data = data + key + ','
    values = values + '"' + value + '",'
  });
  const data_query = data.substring(0, data.length - 1) + ')'
  const values_query = values.substring(0, values.length - 1) + ')'
  
  const query = 'INSERT INTO user_post ' + data_query + ' VALUES ' + values_query
  connection.query(query, function (err, rows, fields) {
    if (err) res.status(400).send('0')
    res.status(200).send(rows.affectedRows.toString())
    
  })
})

app.get('/update-data-post', (req, res) => {
  let create_query = ''
  let data_where = ''
  Object.entries(req.query).forEach(entry => {
    const [key, value] = entry;
    const column = key + '= "' + value + '",'
    if (key === 'id') {
      data_where = column.substring(0, column.length - 1)
    } else {
      create_query = create_query + column
    }
  });
  const data_query = create_query.substring(0, create_query.length - 1) 
  
  const query = 'UPDATE user_post SET ' + data_query + ' WHERE ' + data_where
  console.log(query)
  connection.query(query, function (err, rows, fields) {
    if (err) res.status(400).send('0')
    res.status(200).send(rows.affectedRows.toString())
  })

})

app.get('/delete-data-post', (req, res) => {
  let data_where =  'id = "' + req.query['id'] + '"'
  
  const query = 'DELETE FROM user_post WHERE ' + data_where
  console.log(query)
  connection.query(query, function (err, rows, fields) {
    if (err) res.status(400).send('0')
    res.status(200).send(rows.affectedRows.toString())
  })

})



app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})

app.get('/', (req, res) => {
    console.log('hola')
    res.sendFile(renderHTML)
})