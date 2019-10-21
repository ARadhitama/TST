# Loot Box API
Teknologi Sistem Terintegrasi\
Ariq Radhitama Ariasatya - 18217017

## Setup (Windows)

```bash
# install enviroments
$ py -3 -m venv venv
$ venv\Scripts\> activate
(venv) $ pip install -r requirements.txt
```

## Running Locally (Windows)

```bash
# default https://localhost:5000
$ venv\Scripts\> activate
(venv) $ py main.py

# leaving venv
(venv) $ deactivate
```

## Database

```bash
# create database
(mariadb) $ CREATE DATABASE lootbox;

# create table
(mariadb) $ CREATE TABLE box (idBox VARCHAR(255) NOT NULL PRIMARY KEY AUTO INCREMENT, name VARCHAR(255) NOT NULL);
(mariadb) $ CREATE TABLE items (idItem VARCHAR(255) NOT NULL PRIMARY KEY, itemName VARCHAR(255) NOT NULL, percentage INT NOT NULL, FOREIGN KEY (idBox) REFERENCES box(idBox));
```