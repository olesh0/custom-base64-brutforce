import os
import json

from simple_term_menu import TerminalMenu
from menu import initial_actions, handlers

default_files_directory = "cipher_files/"


def retrieve_labels(actions):
  mapped = map(lambda action: action.get('label'), actions)

  return list(mapped)


def get_path_string(path_array):
  path_string = ""

  for item in path_array:
    path_string += item + " > "

  return path_string


def ask_data(action, sub_elements_path = []):
  DEFAULT_LABEL = "What you wanna do?"

  sub_items = action.get('sub_items', [])

  selected_subitem = show_entries(
    retrieve_labels(sub_items),
    label = get_path_string(sub_elements_path)
  )
  selected = sub_items[selected_subitem]

  selected_sub_items = selected.get('sub_items', {})

  if len(selected_sub_items) > 0:
    return ask_data(
      selected,
      sub_elements_path = sub_elements_path + [selected.get('label', '')]
    )

  files = selected.get('files', [])
  data_list = selected.get('data', [])

  files_input = {}
  data_input = {}

  for file_item in files:
    reason = file_item.get("reason", "We need a file...")
    name = file_item.get("name", None)

    files_input[name] = ask_file(label=reason)

  for data_item in data_list:
    reason = data_item.get("reason", "We need a file...")
    name = data_item.get("name", None)

    data_input[name] = input(reason)

  selected["files"] = files_input
  selected["data"] = data_input

  return selected


def show_entries(entries_list, label = "Select something..."):
  terminal_menu = TerminalMenu(entries_list, title=label)
  return terminal_menu.show()


def ask_file(directory = default_files_directory, label = "Which file?"):
  files = os.listdir(directory)
  files_with_back = [".."] + files

  file_index = show_entries(files_with_back, label = label)
  selected_file = os.path.join(directory, files_with_back[file_index])

  if os.path.isdir(selected_file):
    return ask_file(directory=selected_file)

  return selected_file


def main():
  data = ask_data(initial_actions, ["Main menu"])

  handler = data.get("handler", None)

  if handler:
    files_data = data.get("files", [])
    input_data = data.get("data", [])

    # Running assigned handler
    handlers[handler](files_data | input_data)
  else:
    print("No handler found for", data.get('label'))

  print("================ DEBUG INFO =================")
  print(print(json.dumps(data, indent = 2)))


if __name__ == "__main__":
  main()
