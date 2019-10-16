from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Servers running'

if __name__ = "__main__":
    app.run(ssl_context=('csr.txt','private-key.key'))