import pyAesCrypt as pe
import os

buff = 64*1024


def encrypt (filename, password):
    if "CRYPT" in filename:
        return
    else:
        pe.encryptFile(filename,filename+'.CRYPT',password,buff)
        os.remove(filename)


def decrypt (filename, password):
    filename = filename + '.CRYPT'
    if "CRYPT" in filename:
        pe.decryptFile(filename,filename[:-6],password,buff)
        os.remove(filename)
    else:
        return

if __name__ == '__main__':
    decrypt('input.txt.AES', 'butcher')
