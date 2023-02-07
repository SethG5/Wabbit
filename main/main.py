#######################
# WABBIT
# A PROJECT BY SETH GRAHAM
# I AM NOT RESPONSIBLE FOR YOUR USE OF THIS PROGRAM
#######################

#######################
# TODO
#######################

#Clean'hashid.py'
#RandomHashBrute
#OrderedHashBrute
#WordlistHashBrute
#OnlineBrute
#dir brute

#######################
# IMPORTS
#######################

import os
import webbrowser
from platform import system
from time import sleep
import hashlib
from modules import AntHashLib
import random
import socket
from builtins import input
from sys import argv, exit

#######################
# MODULE IMPORT
#######################

from modules import hashid

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
          hashid.hashid(hash)
      except IndexError:
        print('Usage: hashid [hash]')
    if mainCommand == 'hash':
      try:
        string = command[1]
        hashType = command[2]
        hashType = hashType.lower()
        string = AntHashLib.String(string)
        exec(f'print(string.{hashType}())')
      except AttributeError:
        print('Hash not found.')
      except SyntaxError:
        print('Error, put the hashtype in plain text')
      except IndexError:
        print('Usage: hash [string] [hashType]')


#######################
# RUN
#######################

    if mainCommand == 'wizard':
      print('not finished yet')
    if mainCommand == 'help':
      print('''
      hashid [hash]            | identifies possible hashes
      hash [string] [hashType] | hashes a string
      help                     | take a guess
      wizard                   | Opens a more simple version of Wabbit
      ''')
    else:
      print('Command not found. Try running help.)
if __name__ == '__main__':      
  main()
  
