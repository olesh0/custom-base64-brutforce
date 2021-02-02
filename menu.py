def encode_file(data):
  print("ENCODING FILE...", data)

  return True

handlers = {
  "encode_file": encode_file,
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
