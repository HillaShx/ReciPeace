# import mysql.connector
from flask import Flask
import mysql.connector

recipe_db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="Recipease"
)

"""
===MYSQL===

$$to make a new mysql container$$
docker run --detach --name=test-mysql -v /home/hillash/Documents/SheCodes-Project/mysql-local:/var/lib/mysql --env="MYSQL_ROOT_PASSWORD=root" --publish 3306:3306 mysql

$$to run the mysql container$$
docker container start e2
('e2' or whatever the first 2 characters of the container id are)

$$to connect to the mysql container bash$$
docker exec -it e2 /bin/bash
('e2' or whatever the first 2 characters of the container id are)
mysql -uroot -p
root

===FLASK===
export FLASK_APP=main.py
export FLASK_DEBUG=1
flask run
"""



app = Flask(__name__)

app.config['SECRET_KEY'] = '07979268f0f831f0c013f6b04632d962'

from RecipEase import routes
