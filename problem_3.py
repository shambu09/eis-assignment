import os

def n_process(n):
    parent_id = os.getpid()
    for i in range(n):
        if os.getpid() == parent_id:
            os.fork()

    if os.getpid() != parent_id:
        print(os.getpid())

if __name__ == "__main__":
    n_process(10)