from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    return 'Essa é a HomePage'

@app.route('/contatos')
def contatos():
    return 'Esses são meus contatos'

app.run()
