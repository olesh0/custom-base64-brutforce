from simple_term_menu import TerminalMenu

initial_actions = ["Encode file", "Decode file", "Brutforce string", "Brutforce file"]


def show_entries(entries_list, label = ""):
  terminal_menu = TerminalMenu(entries_list, title=label)
  return terminal_menu.show()


def main():
  action = show_entries(
    initial_actions,
    label="What you wanna do?"
  )

  print(action, initial_actions[action])


if __name__ == "__main__":
  main()
