from flask import Flask, render_template, jsonify
import AES
import RSA
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
    print(file)
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
    file = request.args.get('filename')
    pwd = open('crypt//asd.txt').read()
    print(pwd)
    result = True
    try:
        RSA.keys_generate(1024)
        RSA.encrypt_RSA('static//files//' + file)
    except Exception as e:
        print(e)
        result = False
    return jsonify({'success': result})

@app.route('/generate_keys')
def gen_keys():
    pwd = request.args.get('pwd')
    result = True
    try:
        f = open('crypt//asd.txt', 'w')
        f.write(pwd)
        f.close()
    except Exception as e:
        print(e)
        result = False
    return jsonify({'success': result})


if __name__ == '__main__':
    app.run(debug=True, use_debugger=False, use_reloader=False, passthrough_errors=True)