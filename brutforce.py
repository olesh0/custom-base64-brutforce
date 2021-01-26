from os.path import exists

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


if __name__ == "__main__":
  words_to_expect_raw = input("Words to expect (divided by |): ")
  words_to_expect = words_to_expect_raw.split('|')

  way_to_go = ask_options(
    possible_options=["f", "s"],
    label="Wanna do a file or just paste a string? [f/s] ",
    validate=check_file_exists
  )

  stop_when_word_matched = ask_options(
    possible_options=["Y", "n"],
    label="Wanna stop as soon as one word matched? [Y/n]: ",
    default="y"
  )

  print("FYI:", "stop then single word matched" if stop_when_word_matched == "y" else "never stop")
  print(words_to_expect)

  if way_to_go == "f":
    string_to_brutforce = cipher_file_content
    print(f"The length of the cipher file is {len(cipher_file_content)} characters")
  else:
    print(f"There is the string to brutforce: {string_to_brutforce}")

  # TODO Finally start brutforcing the string
