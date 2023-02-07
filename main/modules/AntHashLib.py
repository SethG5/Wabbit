import hashlib

class String:
  def __init__(self, string):
    self.string = ''

  def sha1(self):
    result = hashlib.sha1(self.string.encode())
    return result.hexdigest()

  def sha224(self):
    result = hashlib.sha224(self.string.encode())
    return result.hexdigest()

  def sha256(self):
    result = hashlib.sha256(self.string.encode())
    return result.hexdigest()
    
  def sha384(self):
    result = hashlib.sha384(self.string.encode())
    return result.hexdigest()
    
  def sha512(self):
    result = hashlib.sha512(self.string.encode())
    return result.hexdigest()

  def blake2b(self):
    result = hashlib.blake2b(self.string.encode())
    return result.hexdigest()
    
  def blake2s(self):
    result = hashlib.blake2s(self.string.encode())
    return result.hexdigest()

  def md5(self):
    result = hashlib.md5(self.string.encode())
    return result.hexdigest()

  def sha3_224(self):
    result = hashlib.sha3_224(self.string.encode())
    return result.hexdigest()

  def sha3_384(self):
    result = hashlib.sha3_384(self.string.encode())
    return result.hexdigest()

  def sha3_512(self):
    result = hashlib.sha3_512(self.string.encode())
    return result.hexdigest()

  def shake_128(self):
    result = hashlib.sha3_512(self.string.encode())
    return result.hexdigest()

  '''def shake_256(self):
    result = hashlib.shake_256(self.string.encode())
    return result.hexdigest()'''
