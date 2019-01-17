from flask import Flask, render_template, jsonify
import AES
# import RSA
from flask import request
app = Flask(__name__)

@app.route('/')
def hello_world():
    print('index')
    return render_template('index.html')


@app.route('/encrypt')
def encrypt():
    file = request.args.get('filename')
    pwd = open('crypt//asd.txt').read()
    print(pwd)
    result = True
    try:
        AES.encrypt('static//files//' + file, pwd)
    except Exception as e:
        print(e)
        result = False
    return jsonify({'success':result})


@app.route('/decrypt')
def decrypt():
    file = request.args.get('filename')
    pwd = open('crypt//asd.txt').read()
    print(pwd)
    result = True
    try:
        AES.decrypt('static//files//' + file, pwd)
    except Exception as e:
        print(e)
        result = False
    return jsonify({'success':result})


@app.route('/sign')
def sign():
    return 'Sign'


if __name__ == '__main__':
    app.run(debug=True, use_debugger=False, use_reloader=False, passthrough_errors=True)