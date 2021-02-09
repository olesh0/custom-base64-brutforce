import brutforce
from encode_file import encode_file
from decode_file import decode_file
from custombase64 import encode_process, decode_process

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
  iteration_start = handle_integer_input(data.get('iteration_start', 0), default=0)

  brutforce.set_cipher_file(file_path)
  brutforce.apply_brutforce(words_to_expect=words_to_expect, start=iteration_start)


def string_brutforce_handler(data):
  brutforce_string = data.get('brutforce_string', None)

  if not brutforce_string:
    print("You must specify a string to brutforce.")
    return

  words_to_expect = data.get('words_to_expect', None)
  iteration_start = handle_integer_input(data.get('iteration_start', 0), default=0)

  brutforce.string_to_brutforce = brutforce_string
  brutforce.apply_brutforce(words_to_expect=words_to_expect, start=iteration_start)


def handle_integer_input(raw_input, default = None, log = True):
  if len(raw_input) > 0:
    try:
      return int(raw_input)
    except:
      if log: print(f"Unknown value has been passed. Using default ({default})")
      return default
  else:
    return default


handlers = {
  "encode_file": encode_file_handler,
  "encode_string": encode_string,
  "decode_file": decode_file_handler,
  "decode_string": decode_string_handler,
  "brutforce_file": brutforce_file_handler,
  "string_brutforce_handler": string_brutforce_handler,
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
            { 'reason': 'Words to expect in decrypted text [divided by | ]:', 'name': 'words_to_expect' },
            { 'reason': 'Iteration start [0]: ', 'name': 'iteration_start' },
          ],
        },
        {
          'label': "Brutforce a string",
          'handler': "string_brutforce_handler",
          'data': [
            { 'reason': 'Words to expect in decrypted text [divided by | ]:', 'name': 'words_to_expect' },
            { 'reason': "String to brutforce: ", 'name': 'brutforce_string' },
            { 'reason': 'Iteration start [0]: ', 'name': 'iteration_start' },
          ],
        },
      ],
    },
  ],
}
