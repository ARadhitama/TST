# Loot Box API
Teknologi Sistem Terintegrasi\
Ariq Radhitama Ariasatya - 18217017

## Setup (Windows)

```bash
# install enviroments
$ py -3 -m venv venv
$ venv\Scripts\> activate
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
(mariadb) $ CREATE TABLE box (idBOX INT NOT NULL PRIMARY KEY, name VARCHAR(10) NOT NULL);
(mariadb) $ CREATE TABLE items (itemName VARCHAR(20) NOT NULL PRIMARY KEY, persentase INT NOT NULL);
(mariadb) $ CREATE TABLE box_items (id INT NOT NULL, name VARCHAR(20) NOT NULL, PRIMARY KEY(id,name));
```