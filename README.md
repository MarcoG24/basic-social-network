Error in planetscaled when "react-scripts" version > "4.0.3",

# Posibles mejoras
- deuda tecnica
- front
- conexion segura con apis
- enviar json por api para no enviar toda la data en el url
- mejorar naming en base de datos
- codigo más limpio y tipado
- manejar un solo estilo para los formularios
- tener carga de imagenes en formularios al crear publicaciones
- hacer logout
- normalizar comillas simples o dobles
- ordenar post del más nuevo al más viejo
- cuando den like, mostrar animación 
- mostrar cuantos hits (+1) tiene cada publicación
- mejorar front y mostrar quien hizo la publicación
# Basic Social Network

This project is divided into 2 subprojects:

## APIs

Contains the following technologies:
* dotoenv
* mysql2
* express

## System

Contains the following technologies
* flask (python)
* javascript
* ajax

## PlanetScale used as database

* create table "users":
```
CREATE TABLE `users` (
  `email` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `type_user` varchar(100) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
```

* create table "user_post":
```
CREATE TABLE `user_post` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title_post` varchar(250) DEFAULT NULL,
  `subtitle` varchar(250) DEFAULT NULL,
  `note` varchar(500) DEFAULT NULL,
  `user` varchar(250) DEFAULT NULL,
  `date` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
```

# To run the project you need to have python 3 installed and:

* Download repository

* Install libraries

- python
`pip install flask`

- install nodejs and
`npm i package.json`

* Create .env file inside the "api-connection" folder and add planetScale database credentials
from a new console `cd [folder-name]/api-connection`
`node conn.js`

* run system
`cd [folder-name]`
` flask run `


