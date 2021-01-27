import math
from os.path import exists
from progress.bar import Bar

cipher_file_content = None
string_to_brutforce = None

def check_file_exists(answer):
  if answer == "f":
    file_path = input("File path: ")

    if not file_path:
      return False

    if not exists(file_path):
      print("Such file doesn't exist...")
      return False

    global cipher_file_content
    cipher_file_content = open(file_path, mode='r').read()

    return True
  elif answer == "s":
    global string_to_brutforce
    string_to_brutforce = input("String to brutforce: ")

    return len(string_to_brutforce) > 0

  return False

def ask_options(possible_options, label, validate = None, default = None):
  do_again = lambda : ask_options(
    possible_options=possible_options,
    label=label
  )

  answer = input(label)

  if validate and not validate(answer):
    return do_again()

  if not answer and default:
    return default

  if not answer or answer not in possible_options:
    return do_again()

  return answer

# ['a', 'b', 'c', 'd', 'e', 'f', 'g']


def place_character(key, character, place_index):
  new_key = list(key)
  filtered_key = []

  for index, value in enumerate(new_key):
    if index == place_index:
      filtered_key.append(character)

    if value != character:
      filtered_key.append(value)

  return "".join(filtered_key)


if __name__ == "__main__":
  words_to_expect_raw = input("Words to expect (divided by |): ")
  words_to_expect = words_to_expect_raw.split('|')

  # way_to_go = ask_options(
  #   possible_options=["f", "s"],
  #   label="Wanna do a file or just paste a string? [f/s] ",
  #   validate=check_file_exists
  # )

  string_to_brutforce = "FsTT7r7xysoMjrV87rVLW/tuGwI0hkKuGYeHGvhRb2I0W/XAykl8j/hR"

  stop_when_word_matched = ask_options(
    possible_options=["Y", "n"],
    label="Wanna stop as soon as one word matched? [Y/n]: ",
    default="y"
  )

  print("FYI:", "stop then single word matched" if stop_when_word_matched == "y" else "never stop")
  print(words_to_expect)

  # if way_to_go == "f":
  #   string_to_brutforce = cipher_file_content

  print("#### starting brutforce process ####")

  matched_word = None
  iteration = 1

  key = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

  possible_options_count = math.factorial(len(key))

  print(f"Key length is {len(key)}")

  with Bar('Processing', max=possible_options_count, suffix='%(percent)d%%') as bar:
    # Moving each character along the string, so there's each posibility included
    while matched_word == None:
      character_to_move = math.floor(iteration / len(key))
      new_place = iteration - (character_to_move * len(key))

      # TODO Investigate "string index out of range" on 4096 iteration

      print({
        'new_place': new_place,
        'character_to_move': character_to_move,
        'iteration': iteration,
      })

      character = key[character_to_move]

      key_to_decode = place_character(
        key=key,
        character=character,
        place_index=new_place
      )

      iteration += 1
      # bar.suffix = f"Processing key {key_to_decode} matches: {0}"
      # bar.next()
