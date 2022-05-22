from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.Util.number import *
import random

#######
BUFFER_LEN = 16

#######
class dataSecurity:
  def __init__(self):
    pass

  def addPadding(self, data: str):
    pad = b'\x00'*(BUFFER_LEN - (len(data)%BUFFER_LEN))
    newData = data+pad
    return newData

  def remPadding(self, data: str):
    padBegLoc = data.index(b'\x00')
    newData = data[:padBegLoc]
    return newData

  ##########

  def getDesiredLen(self, data: str, reqLen: int=BUFFER_LEN):
    data  = data.encode()
    data = data[:reqLen]
    return data

  def genDesiredAES(self, passHash: str, pos: int=BUFFER_LEN):
    # get key & vi str
    midPass = passHash[pos:-1*(pos)]
    key = midPass[:pos]
    iv = midPass[pos:]
    ## pick required part
    key = self.getDesiredLen(key)
    iv = self.getDesiredLen(iv)
    # get AES obj
    aes = AES.new(key, AES.MODE_CBC, iv)
    return aes

  ##########

  def encryptData(self, data: str, passw: str):
    aes = self.genDesiredAES(passw)
    ## padding
    data = data.encode()
    data = self.addPadding(data)
    ## encrypting
    encData = aes.encrypt(data)
    return encData

  def decryptData(self, data: bytes, passw: str):
    aes = self.genDesiredAES(passw)
    ## decrypting
    decDataPadded = aes.decrypt(data)
    ## padding
    decData = self.remPadding(decDataPadded)
    decData = decData.decode('utf8')
    return decData