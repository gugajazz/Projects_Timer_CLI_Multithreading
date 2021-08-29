import threading
import time
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)  # makes color work on win

active_project = 'None'
projects = {'None': 0}


def clock():
    while True:
        if active_project == 'None':
            time.sleep(1)
        else:
            projects[active_project] += 1
            time.sleep(1)
            # print(f'{clock_time}')


def menu():
    global active_project

    while True:
        print(Back.BLUE + Fore.LIGHTWHITE_EX + "(1)" + Style.RESET_ALL + " See current project's time\n" +
              Back.BLUE + Fore.LIGHTWHITE_EX + "(2)" + Style.RESET_ALL + " See all projects\n" +
              Back.BLUE + Fore.LIGHTWHITE_EX + "(3)" + Style.RESET_ALL + " Change active project\n" +
              Back.BLUE + Fore.LIGHTWHITE_EX + "(4)" + Style.RESET_ALL + " Add project\n" +
              Back.BLUE + Fore.LIGHTWHITE_EX + "(5)" + Style.RESET_ALL + " Remove project\n" +
              Back.BLUE + Fore.LIGHTWHITE_EX + "(6)" + Style.RESET_ALL + " Exit")

        option = input("--> ")

        if option == '1':
            print(f"\nActive project: {Back.MAGENTA + Fore.LIGHTWHITE_EX}{active_project}{Style.RESET_ALL}\n" +
                  f"Time elapsed: {Back.MAGENTA + Fore.LIGHTWHITE_EX}{projects[active_project]} seconds" +
                  f"{Style.RESET_ALL}\n")

        elif option == '2':
            for p in projects:
                print(f"\nName: {Back.MAGENTA + Fore.LIGHTWHITE_EX}{p}{Style.RESET_ALL}\n" +
                      f"Time elapsed: {Back.MAGENTA + Fore.LIGHTWHITE_EX}{projects[p]} seconds{Style.RESET_ALL}")

            print("")  # adds newline

        elif option == '3':
            for p in projects:
                print(f"\nName: {Back.MAGENTA + Fore.LIGHTWHITE_EX}{p}{Style.RESET_ALL}\n" +
                      f"Time elapsed: {Back.MAGENTA + Fore.LIGHTWHITE_EX}{projects[p]} seconds{Style.RESET_ALL}")

            proj_name = input("\nInput the project name: ")
            print("")

            if proj_name == 'None':
                if proj_name == active_project:
                    print(Back.RED + Fore.LIGHTWHITE_EX + "That project is already active\n")
                else:
                    active_project = proj_name

            elif proj_name in projects:
                if proj_name == active_project:
                    print(Back.RED + Fore.LIGHTWHITE_EX + "That project is already active\n")
                else:
                    active_project = proj_name

            else:
                print(Back.RED + Fore.LIGHTWHITE_EX + "Incorrect Project Name\n")

        elif option == '4':
            proj_name = input("\nInput the project name: ")
            if proj_name in projects:
                print(Back.RED + Fore.LIGHTWHITE_EX + "\nA project with that name already exists\n")
            else:
                projects[proj_name] = 0  # add project to dictionary
                print("")

        elif option == '5':
            for p in projects:
                print(f"\nName: {Back.MAGENTA + Fore.LIGHTWHITE_EX}{p}{Style.RESET_ALL}\n" +
                      f"Time elapsed: {Back.MAGENTA + Fore.LIGHTWHITE_EX}{projects[p]} seconds{Style.RESET_ALL}")

            proj_name = input("\nInput the project name: ")
            print("")

            if proj_name == 'None':
                print(Back.RED + Fore.LIGHTWHITE_EX + "Cant delete None\n")

            elif proj_name in projects:
                if proj_name == active_project:  # if you delete the current active project
                    active_project = 'None'
                del projects[proj_name]

            else:
                print(Back.RED + Fore.LIGHTWHITE_EX + "Incorrect Project Name\n")

        elif option == '6':
            print(Back.MAGENTA + Fore.LIGHTWHITE_EX + "\nGoodbye")
            colorama.deinit()  # stops using colorama
            exit(1)

        else:
            print(Back.RED + Fore.LIGHTWHITE_EX + "\nIncorrect Input\n")


if __name__ == '__main__':
    clock_thread = threading.Thread(target=clock)
    clock_thread.setDaemon(True)
    clock_thread.start()
    # print("Clock Process Started\n")

    menu()
