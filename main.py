from flask import Flask, render_template
from flask_mysqldb import MySQL
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'MyDB'

mysql = MySQL(app)

@app.route('/lootbox', methods =['POST'])
def lootbox():
    return render_template('UI\index.html')

@app.route('/lootbox/<int:idBox>', methods =['GET', 'PUT'])
def lootbox(idBox):
    return render_template('UI\index.html')

@app.route('/item/<int:idBox>', methods =['GET'])
def item(idBox):
    return render_template('UI\index.html')

if __name__ = "__main__":
    app.run(ssl_context=('csr.txt','private-key.key'))  