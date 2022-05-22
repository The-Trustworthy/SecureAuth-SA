## library
import binascii
import base64
import hashlib
from os import strerror
import numpy as np
from PIL import Image,ImageOps

##  data preparation class
class dataProcessor:
  def __init__(self):
    return
  
  def getNumericStr(self, gotStr: str):
    strBytes = gotStr.encode()
    hexStr = binascii.hexlify(strBytes)
    strNum = hexStr.decode('utf8')
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
  
  ##########################
  
  def getSHA256(self, data: str):
    encData=data.encode()
    dataHash = hashlib.sha256(encData)
    dataHashStr = dataHash.hexdigest()
    return dataHashStr
  
  ##########################
  
  def processBiometric(self, fileName: str):
    try:
      im = Image.open(fileName)
      im = ImageOps.grayscale(im)
      imarr = np.array(im)
      imarr = imarr.reshape(imarr.shape[0]*imarr.shape[1],)
      bioFPStr = str(sum(imarr))
      # fp hash (sha 256)
      fpHashStr = self.getSHA256(bioFPStr)
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
      dobProdHash = self.getSHA256(dobProduct)
    except:
      print("Invalid DoB!!")
      dobProdHash = False
    finally:
      return dobProdHash
  
  def processPass(self, password: str):
    try:
      passNumStr = self.__getNumericStr(password)
      passNumHash = self.getSHA256(passNumStr)
    except:
      print("Invalid Password!!")
      passNumHash = False
    finally:
      return passNumHash

  ##########################
  
  __mapToSingleDigit = mapToSingleDigit
  __getNumericStr = getNumericStr

#########################
#########################

class secureAuth(dataProcessor):
  def __init__(self):
    super().__init__()
    return
  
  def getHexInt(self, data: str):
    dataBytes = data.encode()
    dataHex = binascii.hexlify(dataBytes)
    dataHexInt = int(dataHex)
    return dataHexInt

  ############

  def getEffectivePass(self, passw: str, DoB=False, fpData==False):
    if not DoB:
      DoB = "17/08/1997"      
    ## pre processing
    DoB = self.processDOB(DoB)
    if fpData:
      fpData = self.processBiometric(fpData)
    else:
      fpData = "c44606cd2a6f9de10a539dcf25a6ddb658390d8d670e365d3ef7f904195c1491"
    passw = self.processPass(passw)
    ## hex value
    DoB = self.__getHexInt(DoB)
    fpData = self.__getHexInt(fpData)
    passw = self.__getHexInt(passw)
    ## XORing
    fpXORPass = fpData ^ passw
    fpXORPassDoB = fpXORPass ^ DoB
    effPassXOR = str(fpXORPassDoB)
    ## effective HASH
    effPassHash = self.getSHA256(effPassXOR)
    return effPassHash
  
  #################

  __getHexInt = getHexInt