import custombase64
from brutforce import ask_options
from os import path


def ask_key():
  key = input("What's your key? ")

  if not key:
    return ask_key()

  return key


def ask_file_path():
  file_path = input("File path: ")
  file_exists = path.exists(file_path)

  if not file_exists:
    ask_file_path()

  return file_path


def main():
  file_path = "cypher_files/secret_song" # ask_file_path()

  file = open(file_path, "r")
  data = file.read()

  custombase64.show_key = True
  custombase64.randset("ignore this")

  encoded = custombase64.dataencode(data)
  encoded_prettified = ""


  for index, letter in enumerate(encoded):
    if index % 80 == 0 and index > 0:
      encoded_prettified += "\n"

    encoded_prettified += letter


  encrypted_file_path = f"{file_path}.cypher"

  encrypted_file = open(encrypted_file_path, "w+")
  encrypted_file.write(encoded_prettified)

  print("=============================")
  print(f"Here's your key: {custombase64.cuscharset}")
  print("=============================")

  print(f"Encoded. The result is written into ==>> {encrypted_file_path}")


if __name__ == '__main__':
  main()
