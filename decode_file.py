import custombase64
from brutforce import ask_options
from os import path

default_file_path = "cypher_files/default.cypher"


def ask_key():
  key = input("What's your key? ")

  if not key:
    return ask_key()

  return key


def ask_file_path():
  file_path = input("File path: ")
  file_exists = path.exists(file_path)

  if not file_exists:
    default_file = ask_options(
      possible_options=["y", "n"],
      label="Seems like file doesn't exist. Want to try default file? [y/N]",
      default="n",
    ) == "y"

    if default_file:
      return default_file_path

    ask_file_path()

  return file_path


def decode_file(file_path, key):
  if not path.exists(file_path):
    print("File does not exist.")

    return None

  file = open(file_path, "r")
  data = file.read()

  custombase64.set_charset(key)
  decoded = custombase64.datadecode(data).decode()

  decrypted_file_path = f"{file_path}.decrypted"

  decrypted_file = open(decrypted_file_path, "w+")
  decrypted_file.write(decoded)

  return {
    'decoded': decoded,
    'path': decrypted_file_path,
  }


def main():
  file_path = ask_file_path()
  key = ask_key()

  decryption = decode_file(file_path, key)

  if not decryption:
    return

  print("=============================")
  print(decryption.get('decoded'))
  print("=============================")

  print(f"Decoded. The result is written into ==>> {decryption.get('path')}")


if __name__ == '__main__':
  main()
