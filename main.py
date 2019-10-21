from flask import Flask, render_template, request, jsonify
from flaskext.mysql import MySQL
app = Flask(__name__)
import request

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'lootbox'

mysql = MySQL()

def response_api(data):
    return(
        jsonify(**data),
        data['code']
    )

@app.errorhandler(x)
def bad_request(e):
    return response_api({

    })

@app.route('/')
def root():
    return 'API using Flask'

@app.route('/lootbox', methods =['POST'])
def lootbox():
    conn = mysql.connect()
    cursor = conn.cursor()

@app.route('/lootbox/<idBox>', methods =['GET', 'PUT'])
global conn, cursor
def lootbox(idBox):
    conn = mysql.connect()
    cursor = conn.cursor()
    if request.method == 'GET' :
        sql = "SELECT itemName, percentage FROM items WHERE idbox=%s"
        cursor.execute(sql,idBox)
        conn.commit()
        res = cursor.fetchall()
    elif request.method == 'PUT' :
        cursor.execute("DELETE FROM items WHERE id=%s",idBox)
        sql = 
        data = ""


@app.route('/item/<int:idBox>', methods =['GET'])
global conn, cursor
def item(idBox):
    conn = mysql.connect()
    cursor = conn.cursor()
    sql = 
    data =  request.args.get('idBox')
    cursor.execute(sql,data)

if __name__ = "__main__":
    app.run(ssl_context=('csr.txt','private-key.key', debug=True))  