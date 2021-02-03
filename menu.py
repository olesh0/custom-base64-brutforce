from encode_file import encode_file
from decode_file import decode_file
from custombase64 import encode_process, decode_process
from brutforce import set_cipher_file, apply_brutforce

def encode_file_handler(data):
  file_path = data.get('encode_file', None)

  print(f"Encrypting file ==>> {file_path}")

  encrypted = encode_file(file_path)

  print(f"Created file at: {encrypted.get('path', 'Unknown path')}")
  print(f"Encrypted with this key: {encrypted.get('key', 'UNKNOWN KEY')}")

  return encrypted

def encode_string(data):
  encode_string = data.get('encode_string', None)

  print(f"Encrypting string ==>> {encode_string}")

  encrypted = encode_process(encode_string=encode_string)

  return encrypted


def decode_file_handler(data):
  file_path = data.get('decode_file', None)
  key = data.get('decode_key', None)

  print(f"Decrypting file ==>> {file_path}")

  decrypted = decode_file(file_path=file_path, key=key)

  print(f"Created decrypted file at: {decrypted.get('path', 'Unknown path')}")

  return decrypted

def decode_string_handler(data):
  decode_string = data.get('decode_string', None)
  key = data.get('decode_key', None)

  print(f"Decrypting string ==>> {decode_string} with key => {key}")

  decrypted = decode_process(cipher_text=decode_string, decode_key=key)

  return decrypted


def brutforce_file_handler(data):
  file_path = data.get('brutforce_file', None)
  words_to_expect = data.get('words_to_expect', None)

  set_cipher_file(file_path)
  apply_brutforce(words_to_expect=words_to_expect)


handlers = {
  "encode_file": encode_file_handler,
  "encode_string": encode_string,
  "decode_file": decode_file_handler,
  "decode_string": decode_string_handler,
  "brutforce_file": brutforce_file_handler,
}

initial_actions = {
  'label': "What you wanna do?",
  'sub_items': [
    {
      'label': "Encode",
      'sub_items': [
        {
          'label': "Encode file",
          'handler': 'encode_file',
          'files': [
            { 'reason': 'Select file to encode', 'name': 'encode_file' }
          ],
        },
        {
          'label': "Encode string",
          'handler': "encode_string",
          'data': [
            { 'reason': "String to encode: ", 'name': 'encode_string' }
          ],
        },
      ],
    },
    {
      'label': "Decode",
      'sub_items': [
        {
          'label': "Decode file",
          'handler': "decode_file",
          'files': [
            { 'reason': 'Select file to decode', 'name': 'decode_file' }
          ],
          'data': [
            { 'reason': "Key for decoding: ", 'name': 'decode_key' },
          ],
        },
        {
          'label': "Decode string",
          'handler': 'decode_string',
          'data': [
            { 'reason': "String to decode: ", 'name': 'decode_string' },
            { 'reason': "Key for decoding: ", 'name': 'decode_key' },
          ],
        },
      ],
    },
    {
      'label': "Brutforce",
      'sub_items': [
        {
          'label': "Brutforce a file",
          'handler': 'brutforce_file',
          'files': [
            { 'reason': 'Select file to encode', 'name': 'brutforce_file' }
          ],
          'data': [
            { 'reason': 'Words to expect in decrypted text [divided by | ]:', 'name': 'words_to_expect' }
          ],
        },
        {
          'label': "Brutforce a string",
          'data': [
            { 'reason': "String to brutforce: ", 'name': 'brutforce_string' }
          ],
        },
      ],
    },
  ],
}
