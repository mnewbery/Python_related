import os
import threading


def print_square(thread_id, num_start: int, num_end: int):
    print("Task assigned to thread {1}: {0}".format(threading.current_thread().name, thread_id))
    print("ID of process running task {1}: {0}".format(os.getpid(), thread_id))
    for i in range(num_start, num_end):
        print("Square: {}".format(i * i))


def print_cube(thread_id, num_start:int, num_end:int):
    print("Task assigned to thread {1}: {0}".format(threading.current_thread().name, thread_id))
    print("ID of process running task {1}: {0}".format(os.getpid(), thread_id))
    for i in range(num_start, num_end):
        print("Cube: {}".format(i * i * i))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    t1 = threading.Thread(target=print_cube, args=(1, 10, 1000))
    t2 = threading.Thread(target=print_square, args=(2, 10, 1000))
    t1.start()
    t2.start()
    t1.join()
    t2.join()



