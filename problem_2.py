import os
import signal

def callback(_, __):
    os.wait()


pid = os.fork()

if pid == 0:
    print(f"Child process : {os.getpid()}")
    print("\n....."*10)

else:
    signal.signal(signal.SIGCHLD, callback)
    print(f"parent process : {os.getpid()}")
    while(1):
        pass