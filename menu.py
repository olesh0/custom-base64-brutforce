from encode_file import encode_file
from decode_file import decode_file
from custombase64 import encode_process

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

handlers = {
  "encode_file": encode_file_handler,
  "encode_string": encode_string,
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
          'files': [
            { 'reason': 'Select file to decode', 'name': 'decode_file' }
          ],
        },
        {
          'label': "Decode string",
          'data': [
            { 'reason': "String to decode: ", 'name': 'decode_string' }
          ],
        },
      ],
    },
    {
      'label': "Brutforce",
      'sub_items': [
        {
          'label': "Brutforce a file",
          'files': [
            { 'reason': 'Select file to encode', 'name': 'brutforce_file' }
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
