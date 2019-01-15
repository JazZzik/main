from flask import Flask, render_template, jsonify
from json import dump
app = Flask(__name__)

@app.route('/')
def hello_world():
    print('index')
    return render_template('index.html')


@app.route('/encrypt')
def encrypt():
    '''if alg == 1:
        #AES
        pass
    else:
        #RSA
        pass'''
    return jsonify({'success':True})


@app.route('/decrypt')
def decrypt():
    '''if alg == 1:
        #AES
        pass
    else:
        #RSA
        pass'''
    return 'decrypt!'


@app.route('/sign')
def sign():
    return 'Sign'


if __name__ == '__main__':
    app.run(debug=True, use_debugger=False, use_reloader=False, passthrough_errors=True)