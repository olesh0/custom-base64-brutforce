# All the respect for this file goes to: https://github.com/kingaling/custombase64

import base64
import random

#  A new custom charset
#  Change this guy to desired string. Append the "=" char if you also want to possibly change its location.
cuscharset = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
#cuscharset = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz+/"
#cuscharset = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ+/"
#cuscharset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/"
#cuscharset = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+/"
#cuscharset = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/"

#  The standard charset
#  If you added an "=" char, or some other char to cuscharst above, make sure to add it here as well.
b64charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

encodedset = str.maketrans(b64charset, cuscharset)
decodedset = str.maketrans(cuscharset, b64charset)


# TODO Say hello to one line return in python which I managed to have forgotten
# + take a look why it wasn't working properly (I'm techically a nood here)
def dataencode(x):
  return base64.b64encode(x.encode())


def datadecode(x):
  translated = x.translate(decodedset)
  decoded = base64.b64decode(translated)

  return decoded


def randset():
  """Generate a random alphabet for use in base64 encoding"""
  x = "".join(random.sample(cuscharset, len(cuscharset)))

  global encodedset
  global decodedset

  encodedset = str.maketrans(b64charset, x)
  decodedset = str.maketrans(x, b64charset)

  if len(cuscharset) == 64:
      print ("New random charset: " + x + "=")
  elif len(cuscharset) == 65:
      print ("New random charset: " + x)

  print ("Record the above string if you ever want to be able to decode this data again.\n")


if __name__ == "__main__":
  # Uncomment the command below to generate a random base64 alphabet.
  randset()

  # print "Type text to encode with random base64 table:"
  plaintext = "random string to encode with base64 custom table encoder/decoder" # input("Put your string to encode into base64 with random table: ")

  #  Encode the plaintext string
  encoded = dataencode(plaintext).decode()
  #enc = 'WGtECM0UDeq9CGs3eHwGriEFqdYIrjgGvdw5qSEGrTkIrTU4vdrFqcEHpjkIqTC4'
  decoded = datadecode(encoded).decode()

  print ("encoded: ", encoded)
  print("decoded: ", decoded)
