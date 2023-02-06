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

class Constant:
  INPUT = f'''\033[31m┌─[{user}\033[1;33m@\033[0;36m\033[31m]─[{dir}]\n└──╼ #'''
  user = socket.gethostname()
  
c = Constant()

#######################
# FUNCTIONS
#######################

def main():
  print(logo)
  print(f'Welcome {user}')
  while True:
    cmdInput = input(c.INPUT)
    command = cmdInput.split(' ')
    mainCommand = command[0].lower()
    if mainCommand == 'hashid':
      if command[1]:
        file = 'wabbit/hashid'
        hash = command[1]
        hashid.hashid(hash)
      else:
        print('Usage: hashid [hash]')

if __name__ == '__main__':      
  main()
  
