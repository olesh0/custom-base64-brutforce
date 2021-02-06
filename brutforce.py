import math
import string
import itertools
from numerize import numerize
from os.path import exists
from progress.bar import Bar

cipher_file_content = None
string_to_brutforce = None
results_file = None


def main():
  global string_to_brutforce

  words_to_expect_raw = "kek|lol" # input("Words to expect (divided by |): ")

  # way_to_go = ask_options(
  #   possible_options=["f", "s"],
  #   label="Wanna do a file or just paste a string? [f/s] ",
  #   validate=check_file_exists
  # )

  # if way_to_go == "f":
  #   string_to_brutforce = cipher_file_content

  string_to_brutforce = "P81pkQl5"

  apply_brutforce(words_to_expect=words_to_expect_raw)


def string_into_list(string):
  return [char for char in string]


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
  iteration = 0

  print("Expecting these words: ", words_to_expect)

  key = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

  possible_options_count = math.factorial(len(key))

  print(f"Key length is {len(key)}")

  print(len(list(itertools.permutations(string_into_list(key), len(key)))))

  return

  with Bar('%(elapsed)ds Processing %(percent).12f%%', max=possible_options_count, suffix='%(percent)d%%') as bar:
    for processing_key_list in itertools.combinations(key, r=len(key)):
      print(iteration)

      if matched_word != None or iteration >= possible_options_count:
        print("I'm done here...")
        break

      processing_key = "".join(processing_key_list)

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


# TODO Make number based (it doesn't try to generate all possible options at once...)
def index_based_permutations(iterable, r=None):
  # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
  # permutations(range(3)) --> 012 021 102 120 201 210
  pool = tuple(iterable)
  n = len(pool)
  r = n if r is None else r

  if r > n:
    return

  indices = list(range(n))
  cycles = list(range(n, n-r, -1))
  yield tuple(pool[i] for i in indices[:r])
  while n:
    for i in reversed(range(r)):
      cycles[i] -= 1
      if cycles[i] == 0:
        indices[i:] = indices[i+1:] + indices[i:i+1]
        cycles[i] = n - i
      else:
        j = cycles[i]
        indices[i], indices[-j] = indices[-j], indices[i]
        yield tuple(pool[i] for i in indices[:r])
        break
    else:
      return


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
