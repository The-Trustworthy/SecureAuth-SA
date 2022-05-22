## library
import binascii
import base64
import hashlib
from os import strerror
import numpy as np
from PIL import Image,ImageOps

##  main class
class preSalting:
  def __init__(self):
    return
  
  def getNumericStr(self, gotStr: str):
    strBytes = gotStr.encode()
    hexStr = binascii.hexlify(strBytes)
    strNum = hexStr.decode('utf8')
    return strNum
  
  def getSHA256(self, data: str):
    encData=data.encode()
    dataHash = hashlib.sha256(encData)
    dataHashStr = dataHash.hexdigest()
    return dataHashStr
  
  def mapToSingleDigit(self, num):
    if len(str(num)) != 1:
      reminder = 0
      while num != 0:
        reminder += num%10
        num //= 10
        res = self.__mapToSingleDigit(reminder)
      return res
    else:
      return num
  
  ##########################
  
  def processBiometric(self, fileName: str):
    try:
      im = Image.open(fileName)
      im = ImageOps.grayscale(im)
      imarr = np.array(im)
      imarr = imarr.reshape(imarr.shape[0]*imarr.shape[1],)
      bioFPStr = str(sum(imarr))
      # fp hash (sha 256)
      fpHashStr = self.__getSHA256(bioFPStr)
    except:
      print("Invalid Fingerprint!!")
      fpHashStr = False
    finally:
      return fpHashStr

  def processDOB(self, dob: str):
    try:
      dob = str(dob)
      dob = dob.split('/')
      dobInt = int(''.join(dob))
      dobUniqueNum = self.__mapToSingleDigit(dobInt)
      dobProduct = str(dobInt * dobUniqueNum)
      dobProdHash = self.__getSHA256(dobProduct)
    except:
      print("Invalid DoB!!")
      dobProdHash = False
    finally:
      return dobProdHash
  
  def processPass(self, password: str):
    try:
      passNumStr = self.__getNumericStr(password)
      passNumHash = self.__getSHA256(passNumStr)
    except:
      print("Invalid DoB!!")
      passNumHash = False
    finally:
      return passNumHash

  ##########################
  
  __mapToSingleDigit = mapToSingleDigit
  __getNumericStr = getNumericStr
  __getSHA256 = getSHA256
  
