import threading
import time
import colorama
from colorama import Fore, Back, Style

colorama.init()  # makes color work on win

active_project = 'None'
projects = {'None': 0}


def clock():
    while True:
        if active_project == 'None':
            file_thread = threading.Thread(target=write_to_file())
            file_thread.setDaemon(True)  # doesn't hang the program when you try and leave
            file_thread.start()
            time.sleep(1)
        else:
            projects[active_project] += 1
            file_thread = threading.Thread(target=write_to_file())
            file_thread.setDaemon(True)  # doesn't hang the program when you try and leave
            file_thread.start()
            time.sleep(1)
            # print(f'{clock_time}')


def read_file():
    file = open("db.txt")
    for line in file:
        key_file, value_file = line.split(" | ")
        value_file = value_file.strip()
        projects[key_file] = int(value_file)


def write_to_file():
    file = open("db.txt", "w")  # deletes everything and writes from beginning

    i = 0
    for project in projects:
        if i == 0:  # doesn't include \n in 1st line
            file.write(f"{project} | {projects[project]}")
        else:  # all other lines
            file.write(f"\n{project} | {projects[project]}")
        i += 1


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

    try:
        read_file()
    except FileNotFoundError:  # if file not found create it
        write_to_file()
    except:
        print(Back.RED + Fore.LIGHTWHITE_EX +
              "db.txt is damaged, if it can't be fixed please delete it and run me again")
        exit(1)

    clock_thread = threading.Thread(target=clock)
    clock_thread.setDaemon(True)  # doesn't hang the program when you try and leave
    clock_thread.start()
    # print("Clock Process Started\n")

    menu()
