import threading

buffer = []  # queue
BUFFER_SIZE = 10
dummy = "dummy object #"

fill_count = threading.Semaphore(0)
avail_count = threading.Semaphore(BUFFER_SIZE)


def produce():
    global buffer
    thread = threading.currentThread().name
    i = 0

    while (i < 10):
        avail_count.acquire()
        buffer.append(dummy + str(fill_count._value))
        i += 1
        print(thread, " buffer: ", buffer)
        fill_count.release()


def consume():
    global buffer
    thread = threading.currentThread().name

    while (True):
        fill_count.acquire()
        buffer.pop()
        print(thread, " buffer: ", buffer, "\n")
        avail_count.release()


producer = threading.Thread(target=produce)
consumer = threading.Thread(target=consume)

print("Main Thread exited", threading.main_thread(), "\n")
producer.start()
consumer.start()
