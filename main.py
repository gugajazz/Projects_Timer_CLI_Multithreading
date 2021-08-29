'''import multiprocessing
import time


def f(d):
    secs = 0
    while True:
        time.sleep(1)
        secs += 1
        d['a'] = secs


def menu():
    p = multiprocessing.Process(target=f, args=(d,))
    p.start()

    while True:
        time.sleep(0.5)
        try:
            print(f"{d['a']}")
        except:
            print("Key error")


if __name__ == '__main__':
    with multiprocessing.Manager() as manager:
        d = manager.dict()
        d['None'] = 0
        p = multiprocessing.Process(target=f, args=(d,))
        p.start()
        time.sleep(1)
        
        while True:
            time.sleep(0.5)
            try:
                print(f"{d['a']}")
            except:
                print("Key erraor")



        #menu()




'''
import multiprocessing
import time


active_project = 'None'
#projects = {'None': 0, 'LOL': 0}



def clock(projects):
    solid_active_project = active_project  # to prevent the change of active_project carring times before thread is killed
    clock_time = projects[solid_active_project]  # start clock where the project already was
    while True:
        clock_time += 1
        time.sleep(1)
        # print(f'{clock_time}')
        projects[solid_active_project] = clock_time


def menu():
    global active_project

    while True:
        print("(1) See current project's time\n(2) Change active project\n(3) Add project\n(4) Exit")
        option = input("--> ")

        if option == '1':
            try:
                print(f"\nActive project: {active_project}\nTime elapsed: {projects[active_project]} seconds\n")
            except:
                print("key error (aaa)\n")

        elif option == '2':
            for p in projects:
                print(f"\nName: {p}\nTime elapsed: {projects[p]} seconds")

            proj_name = input("\nInput the project name: ")

            if proj_name == 'None':
                active_project = proj_name

                try:
                    clock_process.terminate()
                    print("Clock Process Killed\n")
                except UnboundLocalError:
                    print("No Clock Process Running\n")

                print("Done")

            elif proj_name in projects:
                active_project = proj_name

                try:
                    clock_process.terminate()
                    print("Clock Process Killed\n")
                except UnboundLocalError:
                    print("No Clock Process Running\n")

                clock_process = multiprocessing.Process(target=clock, args=(projects,))
                clock_process.start()
                time.sleep(1)
                print("Clock Process Started\n")

            else:
                print("Incorrect Project Name\n")

        elif option == '3':
            proj_name = input("Input the project name: ")
            projects[proj_name] = 0  # add project to dictionary

        elif option == '4':
            try:
                clock_process.terminate()
                print("Clock Process Killed\n")
            except UnboundLocalError:
                print("No Clock Process Running\n")

            exit(1)

        else:
            print("Incorrect Input")


if __name__ == '__main__':
    with multiprocessing.Manager() as manager:
        projects = manager.dict()

        projects['None'] = 0
        projects['lol'] = 0

    menu()
