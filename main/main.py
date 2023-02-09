#######################
# WABBIT
# A PROJECT BY SETH GRAHAM
# I AM NOT RESPONSIBLE FOR YOUR USE OF THIS PROGRAM
#######################

#######################
# TODO
#######################

#Clean'hashid.py'
#OnlineBrute 

#######################
# IMPORTS
#######################

import os
import webbrowser
from platform import system
from time import sleep
import hashlib
import random
import socket
from builtins import input
from sys import argv, exit

#######################
# MODULE IMPORT
#######################

from modules import HashID
from modules import HashBrute
from modules import AntHashLib
from modules import WebBrute
#######################
# VARIABLES
#######################

user = socket.gethostname()
eyes = '-     -'
file = 'wabbit'
dir = '~/' + file

class Constant:
  Prompt = f'''\033[31m┌─[{user}\033[1;33m@\033[0;36m\033[31m]─[{dir}]\n└──╼ $\033[1;37m '''
  user = socket.gethostname()
  logo = '''\033[1;37m
   ***       
  ** **
 **   **
 **   **         **** 
 **   **       **   ****
 **  **       *   **   **
  **  *      *  **  ***  **
   **  *    *  **     **  *
    ** **  ** **        **
    **   **  **
   *           *
  *             *
 *    \033[1;31m-     -\033[1;37m    *
 *   /   @   \   *
 *   \__/ \__/   *
   *     W     *
     **     **   
       *****
       
  '''
  
c = Constant()

#######################
# FUNCTIONS
#######################

def main():
  print(c.logo)
  print(f'Welcome {c.user}\n')
  while True:
    cmdInput = input(c.Prompt)
    command = cmdInput.split(' ')
    mainCommand = command[0].lower()
    if mainCommand == 'hashid':
      try:
        if command[1]:
          hash = command[1]
          HashID.hashid(hash)
      except IndexError:
        print('Usage: hashid [hash]')
    elif mainCommand == 'hash':
      try:
        string = command[1]
        hashType = command[2]
        hashType = hashType.lower()
        string = AntHashLib.String(string)
        print(string.hash(hashType))
      except IndexError:
        print('Usage: hash [string] [hashType]')
    elif mainCommand == 'wizard':
      print('not finished yet')
    elif mainCommand == 'randombrute' or mainCommand == 'rbrute':
      try:
        hash = command[1]
        hashType = command[2]
        hashType = hashType.lower()
        len = command[3]
        len = int(len)
        HashBrute.Random(hash, hashType, False, len)
      except IndexError:
        print('Usage: randombrute [hash] [hashType] [length] [Fixed]')
    elif mainCommand == 'wordlistbrute' or mainCommand == 'wlbrute' or mainCommand == 'wbrute':
      try:
        hash = command[1]
        hashType = command[2]
        hashType = hashType.lower()
        wordlistDir = command[3]
        HashBrute.Wordlist(hash, hashType, wordlistDir)
      except IndexError:
        print('Usage: wordlistBrute [hash] [hashType] [wordlistName.txt]')
    elif mainCommand == 'dirbrute' or mainCommand == 'dbrute':
      try:
        website = command[1]
        wordlist = command [2]
        WebBrute.dir(website, wordlist)
      except IndexError:
        print('Usage: dirbrute [website] [wordlistName.txt]')
    elif mainCommand == 'help':
      print('''
      hashid [hash]                                      | identifies possible hashes of a given hash
      hash [string] [hashType]                           | hashes a given string with the given hash type
      randombrute [hash] [hashType] [length] [Fixed]     | brutes a given hash by randomly generating a password
      wordlistbrute [hash] [hashType] [wordlistName.txt] | brutes a given hash by uing each password in a wordlist
      dirbrute [website] [wordlistName.txt]              | checks a given website for every directory in the wordlist
      wizard                                             | Opens a more simple version of Wabbit
      help                                               | take a guess
      ''')
    else:
      print('Command not found. Try running help.')



#######################
# RUN
#######################

if __name__ == '__main__': 
  try:
    main()
  except KeyboardInterrupt:
    print('The wabbit sleeps...')
    exit()
  
