import custombase64
from brutforce import ask_options
from os import path


def ask_file_path():
  file_path = input("File path: ")
  file_exists = path.exists(file_path)

  if not file_exists:
    ask_file_path()

  return file_path


def encode_file(file_path):
  if not path.exists(file_path):
    print("File does not exist.")

    return None

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


  encrypted_file_path = f"{file_path}.cipher"

  encrypted_file = open(encrypted_file_path, "w+")
  encrypted_file.write(encoded_prettified)

  return {
    'path': encrypted_file_path,
    'key': custombase64.cuscharset,
  }


def main():
  file_path = ask_file_path()

  file_encryption = encode_file(file_path)

  if not file_encryption:
    return

  print("=============================")
  print(f"Here's your key: {custombase64.cuscharset}")
  print("=============================")

  print(f"Encoded. The result is written into ==>> {file_encryption.get('path')}")


if __name__ == '__main__':
  main()
