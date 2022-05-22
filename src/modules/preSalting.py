## library
import binascii
import base64
import hashlib
import numpy as np
from PIL import Image,ImageOps

##  main class
class preSalting:
  def __init__(self):
    return
  
  def getNumericVal(self, gotStr: str):
    strBytes = gotStr.encode()
    hexStr = binascii.hexlify(strBytes)
    strNum = int(hexStr.decode('utf8'))
    return strNum
  
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
  
  def processBiometric(self, fName):
    im = Image.open(fName)
    im = ImageOps.grayscale(im)
    imarr = np.array(im)
    imarr = imarr.reshape(imarr.shape[0]*imarr.shape[1],)
    bioFPStr = str(sum(imarr))
    # fp hash (sha 256)
    encodedFP=bioFPStr.encode()
    fpHash = hashlib.sha256(encodedFP)
    fpHashStr = fpHash.hexdigest()
    res = self.__getNumericVal(fpHashStr)
    return res

  def processDOB(self, dob):
    dob = str(dob)
    dob = dob.split('/')
    dob = int(''.join(dob))
    res = self.__mapToSingleDigit(dob)
    return res
  
  ########

  __mapToSingleDigit = mapToSingleDigit
  __getNumericVal = getNumericVal
  
