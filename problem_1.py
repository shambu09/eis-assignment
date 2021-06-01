import os

def n_process(n):
    parent_id = os.getpid()
    for i in range(n):
        print(os.getpid())
        if os.getpid() == parent_id:
            os.fork()
            
    if os.getpid() != parent_id:
        os._exit(0)

if __name__ == "__main__":
    n_process(10)