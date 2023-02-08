import random
import AntHashLib
def Brute(hash, hashType, Fixed, len):
    cracked == False
    if Fixed == True:
        strLen = len
    elif Fixed == False:
        strLen = random.Randint(1, len)
    for i in range(0, strLen):
        text = random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
    text = AntHashLib.String(text)
    while cracked == False:
        try:
            if hash == text.hash(hashType):
                print("Found: " + text.string)
            else:
                print("Trying: " + text.string)
        except KeyboardInterrupt:
            print("Ending...")
            break
