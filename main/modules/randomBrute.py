import random
from modules import AntHashLib

def Brute(hash, hashType, Fixed, len):
  cracked = False
  if Fixed == True:
      strLen = len
  while cracked == False:
    try:
      text = ''
      if Fixed == False:
        strLen = random.randint(1, len)
      for i in range(0, strLen):
        text += random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()")
      text = AntHashLib.String(text)
      if hash == text.hash(hashType):
        print("Found: " + text.string)
        cracked = True
      else:
        print(f'Trying: {text.hash(hashType)} || {text.string}')
    except KeyboardInterrupt:
        print("Ending...")
        break
