import math
import random
import custombase64
import string
from os.path import exists
from progress.bar import Bar

cipher_file_content = None
string_to_brutforce = None
results_file = None

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


def write_match(result, key):
  global results_file

  if not results_file:
    results_file = open("results.txt", "a")

  results_file.write(f"{key}: {result}\n")


if __name__ == "__main__":
  # words_to_expect_raw = input("Words to expect (divided by |): ")
  # words_to_expect = words_to_expect_raw.split('|')

  # way_to_go = ask_options(
  #   possible_options=["f", "s"],
  #   label="Wanna do a file or just paste a string? [f/s] ",
  #   validate=check_file_exists
  # )

  string_to_brutforce = "rq165PJcRXLSgROa1Cb+"

  stop_when_word_matched = ask_options(
    possible_options=["Y", "n"],
    label="Wanna stop as soon as one word matched? [Y/n]: ",
    default="y"
  )

  print("FYI:", "stop then single word matched" if stop_when_word_matched == "y" else "never stop")

  # if way_to_go == "f":
  #   string_to_brutforce = cipher_file_content

  print("#### starting brutforce process ####")

  matched_word = None
  iteration = 1

  key = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

  possible_options_count = math.factorial(len(key))

  print(f"Key length is {len(key)}")

  with Bar('Processing %(percent).3f%%', max=possible_options_count, suffix='%(percent)d%%') as bar:
    # Moving each character along the string, so there's each posibility included
    while matched_word == None and iteration < possible_options_count:
      guess = random.choices(list(key), k=len(key))
      processing_key = "".join(guess)

      custombase64.set_charset(processing_key)
      decoded = custombase64.datadecode(string_to_brutforce)

      write_match(result=decoded, key=processing_key)
      iteration += 1
      bar.suffix = f"Processing key {processing_key}"
      bar.next()
