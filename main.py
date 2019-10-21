import pymysql
from flask import Flask, request, jsonify
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

@app.errorhandler(400)
def bad_request(e):
    return response_api({
        'code' : 400,
        'message' : 'Kesalahan dalam melakukan request',
        'data' : None
    })

@app.errorhandler(500)
def internal_server_error(e):
    return response_api({
        'code' : 500,
        'message' : 'Gangguan dalam server',
        'data' : None
    })

@app.route('/')
def root():
    return 'API using Flask'

@app.route('/lootbox', methods =['POST', 'PUT'])
def lootbox():
    if request.method == 'POST':
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            _name = request.args.get('name')
            _items = request.args.get('items')
            sql = "INSERT INTO items(itemName, percentage) VALUES (%s,%s)"
            for x in _items:
                data = (x.itemName,x.percentage)
                cursor.execute(sql, data)
            conn.commit()
            _id = "SELECT idBox FROM box ORDER BY idBox DESC LIMIT 1"
            res = {
                'message' : 'Success',
                'id' : _id
            }
            return res
        except Exception as e:
            return e
        finally:
            cursor.close()
            conn.close()
    elif request.method == 'PUT' :
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            _id = request.args.get('idBox')
            _items = request.args.get('items')
            cursor.execute("DELETE FROM items WHERE id=%s",idBox)
            sql = "INSERT INTO items(itemName, percentage) VALUES (%s,%s)"
            for x in _items:
                data = (x.itemName,x.percentage)
                cursor.execute(sql, data)
            conn.commit()
        except Exception as e:
            return e
        finally:
            cursor.close()
            conn.close()
    
@app.route('/lootbox/<idBox>', methods =['GET'])
def lootbox(idBox):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        sql = "SELECT itemName, percentage FROM items WHERE idbox=%s"
        cursor.execute(sql,idBox)
        conn.commit()
        res = cursor.fetchall()
        return response_api(res)
    except Exception as e:
        return e
    finally:
        cursor.close()
        conn.close()

@app.route('/item/<int:idBox>', methods =['GET'])
def item(idBox):
    conn = mysql.connect()
    cursor = conn.cursor()
    data =  request.args.get('idBox')
    cursor.execute(sql,data)

if __name__ == "__main__":
    app.run(ssl_context=('csr.txt','private-key.key'))  