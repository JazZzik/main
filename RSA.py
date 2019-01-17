import rsa, os


def keys_generate(byte):
    (pubkey, privkey) = rsa.newkeys(byte)
    d = open('static\\key\\pubkey.pem', 'wb')
    r = open('static\\key\\privkey.pem', 'wb')
    r.write(privkey.save_pkcs1(format='PEM'))
    d.write(pubkey.save_pkcs1(format='PEM'))
    r.close()
    d.close()


def encrypt_RSA(filename):
    filename = (filename)
    file_pubkey = ('static\\key\\pubkey.pem')
    file = open(filename, 'rb')
    message = file.read()
    file.close()
    file = open(file_pubkey, 'rb')
    pubkey = rsa.PublicKey.load_pkcs1(file.read())
    file.close()
    crypto = rsa.encrypt(message, pubkey)
    s = open(filename+'.rsa', 'wb')
    s.write(crypto)
    s.close()
    os.remove(filename)



def decrypt_RSA(filename):
    filename = (filename + '.rsa')
    file_privkey = ('static\\key\\privkey.pem')
    file = open(filename, 'rb')
    crypto = file.read()
    file.close()
    file = open(file_privkey, 'rb')
    privkey = rsa.PrivateKey.load_pkcs1(file.read())
    file.close()
    message = rsa.decrypt(crypto, privkey)
    s = open(filename[:-4], 'wb')
    s.write(message)
    s.close()
    os.remove(filename)


def sign_rsa(filename):
    filename = ('static\\file' + filename + '.rsa')
    file_privkey = ('static\\key\\privkey.pem')
    signature = rsa.sign(filename, file_privkey, 'SHA-1')