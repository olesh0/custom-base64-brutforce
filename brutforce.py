import math
import random
import string
from numerize import numerize
from os.path import exists
from progress.bar import Bar

cipher_file_content = None
string_to_brutforce = None
results_file = None


def main():
  global string_to_brutforce

  words_to_expect_raw = input("Words to expect (divided by |): ")

  way_to_go = ask_options(
    possible_options=["f", "s"],
    label="Wanna do a file or just paste a string? [f/s] ",
    validate=check_file_exists
  )

  if way_to_go == "f":
    string_to_brutforce = cipher_file_content

  apply_brutforce(words_to_expect=words_to_expect_raw)


def apply_brutforce(words_to_expect = None):
  import custombase64
  global string_to_brutforce

  if not words_to_expect:
    print("No words to expect were set...")
    return None

  if not string_to_brutforce:
    print("No string to brutforce was set...")
    return None

  words_to_expect = words_to_expect.split('|')

  print("#### starting brutforce process ####")

  matched_word = None
  iteration = 1

  print("Expecting these words: ", words_to_expect)

  key = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

  possible_options_count = math.factorial(len(key))

  print(f"Key length is {len(key)}")

  with Bar('%(elapsed)ds Processing %(percent).12f%%', max=possible_options_count, suffix='%(percent)d%%') as bar:
    while matched_word == None and iteration < possible_options_count:
      """
      TODO Never use random.choices for such operations
      There's a big chance some options are being checked a few times (a few million times)
      """
      guess = random.choices(list(key), k=len(key))
      processing_key = "".join(guess)

      custombase64.set_charset(processing_key)
      decoded = custombase64.datadecode(string_to_brutforce)

      decoded_text = str(decoded).lower()

      for word in words_to_expect:
        if len(word) > 0 and word in decoded_text:
          print(f"\nword matched: {word} => {decoded_text}\n")
          write_match(result=decoded_text, key=processing_key)

      iteration += 1
      bar.suffix = f"[{numerize.numerize(iteration, 2)}] Processing key {processing_key}"
      bar.next()


def set_cipher_file(file_path):
  global cipher_file_content
  global string_to_brutforce

  cipher_file_content = open(file_path, mode='r').read()
  string_to_brutforce = cipher_file_content


def check_file_exists(answer):
  if answer == "f":
    file_path = input("File path: ")

    if not file_path:
      return False

    if not exists(file_path):
      print("Such file doesn't exist...")
      return False

    set_cipher_file(file_path)

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
  main()
