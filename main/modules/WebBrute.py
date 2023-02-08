import os
import requests
session = requests.Session()

def dir(website, wordlist):
  os.chdir('Wordlist/')
  foundDirs = []
  with open(wordlist, 'r') as f:
    dirs = str(f.read()).split()
  for dir in dirs:
    try:
      requests.get(f'https://{website}/{dir}')
      if requests.response.status_code == 200:
        foundDirs.append(dir)
        print(f'Found: https://{website}/{dir}')
      else:
        print(f'Trying: https://{website}/{dir}')
    except KeyboardInterrupt:
      print('Ending...')
      break
  print()
  print('Found Directories:')
  for dir in range(foundDirs):
    print(f'{website}/{dir}')
