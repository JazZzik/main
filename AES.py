import pyAesCrypt as pe
import os

buff = 64*1024


def encrypt (filename, password):
    pe.encryptFile(filename,filename+'.AES',password,buff)
    os.remove(filename)


def decrypt (filename, password):
    pe.decryptFile(filename,filename[:-4],password,buff)
    os.remove(filename)


if __name__ == '__main__':
    decrypt('input.txt.AES', 'butcher')
