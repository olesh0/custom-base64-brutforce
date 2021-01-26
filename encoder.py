# All the respect for this file goes to: https://github.com/kingaling/custombase64

import base64
import random

#  A new custom charset
cuscharset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/"

#  The standard charset
#  If you added an "=" char, or some other char to cuscharst above, make sure to add it here as well.
b64charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

encodedset = str.maketrans(b64charset, cuscharset)
decodedset = str.maketrans(cuscharset, b64charset)


def set_charset(new_charset):
  global cuscharset
  cuscharset = new_charset


def dataencode(x):
  encoded = base64.b64encode(x.encode())
  return encoded.decode().translate(encodedset)


def datadecode(x):
  translated = x.translate(decodedset)
  return base64.b64decode(translated)


if __name__ == "__main__":
  # print "Type text to encode with random base64 table:"
  plaintext = "random string to encode with base64 custom table encoder/decoder" # input("Put your string to encode into base64 with random table: ")

  #  Encode the plaintext string
  encoded = dataencode(plaintext)
  #enc = 'WGtECM0UDeq9CGs3eHwGriEFqdYIrjgGvdw5qSEGrTkIrTU4vdrFqcEHpjkIqTC4'
  decoded = datadecode(encoded).decode()

  print ("encoded: ", encoded)
  print("decoded: ", decoded)
