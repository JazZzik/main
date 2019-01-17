import pyAesCrypt as pe
import os

buff = 64*1024


def encrypt (filename, password):
    pe.encryptFile(filename,filename+'.txt.CRYPT',password,buff)
    os.remove(filename)


def decrypt (filename, password):
    filename = filename + '.txt.CRYPT'
    pe.decryptFile(filename,filename[:-10],password,buff)
    os.remove(filename)


if __name__ == '__main__':
    decrypt('input.txt.AES', 'butcher')
