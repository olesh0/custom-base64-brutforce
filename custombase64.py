# All the respect for this file goes to: https://github.com/kingaling/custombase64

import base64
import random
from brutforce import ask_options

show_key = False
text_to_cypher = "random string to encode with base64 custom table encoder/decoder"

#  A new custom charset
cuscharset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/"

#  The standard charset
#  If you added an "=" char, or some other char to cuscharst above, make sure to add it here as well.
b64charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

encodedset = str.maketrans(b64charset, cuscharset)
decodedset = str.maketrans(cuscharset, b64charset)


def main():
  action = ask_options(possible_options=['e', 'd'], label='Encode or decode? [e/d]: ')

  print ("================================")

  if action == 'e':
    encode_process()
  elif action == 'd':
    decode_process()


def encode_process():
  global show_key

  plaintext = input("What shall we cypher [empty for random string]? ")
  show_key = input("Shall we show you the key [y/N]? ").lower() == "y"

  phrase = randset(plaintext)
  encoded = dataencode(text_to_cypher)

  print("========================")

  if show_key:
    print(f"Key: {cuscharset}")

  print ("Cypher text:", encoded)


def decode_process():
  decode_string = input("What shall we decypher? ")
  key = input("What's your key? ")

  set_charset(key)
  decoded = datadecode(decode_string).decode()

  print (f"========== {decoded} ===========")


def set_charset(new_charset):
  global cuscharset
  global encodedset
  global decodedset

  cuscharset = new_charset

  encodedset = str.maketrans(b64charset, cuscharset)
  decodedset = str.maketrans(cuscharset, b64charset)


def dataencode(x):
  encoded = base64.b64encode(x.encode())
  return encoded.decode().translate(encodedset)


def datadecode(x):
  translated = x.translate(decodedset)
  return base64.b64decode(translated)


def randset(text):
  """Generate a random alphabet for use in base64 encoding"""
  global cuscharset
  global encodedset
  global decodedset
  global text_to_cypher

  cuscharset = "".join(random.sample(cuscharset, len(cuscharset)))

  options_to_cypher = [
    "Every prison has a way to escape.",
    "Get busy living, or get busy dying.",
    "Hope is a good thing. May be the best of things.",
    "That's all it takes. Pressure... and time."
  ]

  text_to_cypher = text or random.choice(options_to_cypher)

  encodedset = str.maketrans(b64charset, cuscharset)
  decodedset = str.maketrans(cuscharset, b64charset)

  if not show_key:
    print("\n#############################################\n")
    print("Generated a string with a random key. We won't tell you what this is.\nGood luck brutforcing the result.\n")
    print("* Hint: here are the possible options:")

    for index, option in enumerate(options_to_cypher):
      print(f"  {index + 1}. {option}")

    print("\n#############################################\n")

  return text_to_cypher


if __name__ == "__main__":
  main()
