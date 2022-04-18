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


