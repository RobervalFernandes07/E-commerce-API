from flask import Flask

app = Flask(__name__)

# Define uma rota raiz (página inicial) e a função que será executada ao requisitar.
@app.route('/')
def hello_world():
    return 'Hello, World!'

