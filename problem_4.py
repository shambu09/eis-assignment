import os
import time
import threading

def alt():
    print("---> Before blocking system call\n")
    os.system('date')
    print("---> After blocking system call\n")

alt_thread = threading.Thread(target=alt)
alt_thread.start()

for i in range(10):
    print("Still in main thread......")
print("")
