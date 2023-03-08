# Wabbit
## A CLI password cracking tool written in Python.
### Currently Depricated. Wait for the wabbit 2 (name is tbd)
#### created by Seth. 
---
## Features
- [x] Random Hash Bruting
- [x] Wordlist Hash Bruting
- [x] Hash Identification
- [x] Hashing
- [x] Directory Bruteforcing
- [ ] Server Brute Forcing
- [ ] Website Password BruteForcing
- [ ] Hybrid Brute Forcing
- [ ] Proxy
- [ ] WabbitWizard, a simple CLI version of Wabbit

---
## Usage
not finished yet, so i have no reason to make a Release
but download the code, download the requirements (ill add them later) and run main.py

so far the commands are:

| Command | Usage | Description |
| ----------- | ----------- | ----------- |
| HashID | hashid [hash] | identifies possible hashes of a given hash |
| Hash | hash [string] [hashType] | Hashes the given string with the given hashType |
| Random Brute | randombrute [hash] [hashType] [length] [Fixed] | brutes a given hash by randomly generating a password |
| Wordlist Brute | wordlistbrute [hash] [hashType] [wordlistName.txt] | brutes a given hash by uing each password in a wordlist |
| Directory Brute | dirbrute [website] [wordlistName.txt] | checks a given website for every directory in the wordlist |
| Wizard | wizard | Opens a more simple version of Wabbit |
| Help | help | take a guess |
