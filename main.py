import os
import json

from simple_term_menu import TerminalMenu

default_files_directory = "cypher_files/"

initial_actions = [
  {
    'label': "Encode",
    'sub_items': [
      { 'label': "Encode file", 'need_file': True },
      { 'label': "Encode string", 'need_file': False },
    ],
  },
  {
    'label': "Decode",
    'sub_items': [
      { 'label': "Decode file", 'need_file': True },
      { 'label': "Decode string", 'need_file': False },
    ],
  },
  {
    'label': "Brutforce",
    'sub_items': [
      { 'label': "Brutforce a file", 'need_file': True },
      { 'label': "Brutforce a string", 'need_file': False },
    ],
  },
]


def ask_data(actions_list):
  # action = show_entries(
  #   initial_actions,
  #   label="What you wanna do?"
  # )

  return { 'valuable_message': "Kek lol, I'll finish this one later" }


def show_entries(entries_list, label = ""):
  terminal_menu = TerminalMenu(entries_list, title=label)
  return terminal_menu.show()


def ask_file(directory = default_files_directory):
  files = os.listdir(directory)
  files_with_back = [".."] + files

  file_index = show_entries(files_with_back, label="Which file?")
  selected_file = os.path.join(directory, files_with_back[file_index])

  if os.path.isdir(selected_file):
    return ask_file(directory=selected_file)

  return selected_file


def main():
  data = ask_data(initial_actions)

  print(json.dumps(data, indent = 2))


if __name__ == "__main__":
  main()
