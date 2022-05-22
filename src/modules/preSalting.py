## library
from PIL import Image,ImageOps
import numpy as np

##  main class
class preSalting:
  def __init__(self):
    return
  
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
    ans = sum(imarr)
    res = self.__mapToSingleDigit(ans)
    return res

  def processDOB(self, dob):
    dob = str(dob)
    dob = dob.split('/')
    dob = int(''.join(dob))
    res = self.__mapToSingleDigit(dob)
    return res
  
  ########

  __mapToSingleDigit = mapToSingleDigit
  
