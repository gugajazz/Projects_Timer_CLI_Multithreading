import threading
import time


active_project = 'None'
projects = {'None': 0, 'LOL': 0}


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
        print("(1) See current project's time\n(2) Change active project\n(3) Add project\n(4) Exit")
        option = input("--> ")

        if option == '1':
            print(f"\nActive project: {active_project}\nTime elapsed: {projects[active_project]} seconds\n")

        elif option == '2':
            for p in projects:
                print(f"\nName: {p}\nTime elapsed: {projects[p]} seconds")

            proj_name = input("\nInput the project name: ")

            if proj_name == 'None':
                active_project = proj_name

            elif proj_name in projects:
                active_project = proj_name

            else:
                print("Incorrect Project Name\n")

        elif option == '3':
            proj_name = input("Input the project name: ")
            projects[proj_name] = 0  # add project to dictionary

        elif option == '4':
            exit(1)

        else:
            print("Incorrect Input")


if __name__ == '__main__':
    clock_thread = threading.Thread(target=clock)
    clock_thread.start()
    print("Clock Process Started\n")

    menu()
