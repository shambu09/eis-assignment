import os

child_rStream, parent_wStream = os.pipe()
parent_rStream, child_wStream = os.pipe()

pid = os.fork()

if pid > 0:
    os.close(child_rStream)
    os.close(child_wStream)

    rStream_fo = os.fdopen(parent_rStream)
    print(f"(parent <--- child) : {rStream_fo.read()}")
    os.close(parent_rStream)

    dummy = b"hello!"
    os.write(parent_wStream, dummy)
    os.close(parent_wStream)


else:
    os.close(parent_rStream)
    os.close(parent_wStream)

    dummy = b"hey!"    
    os.write(child_wStream, dummy)
    os.close(child_wStream)

    rStream_fo = os.fdopen(child_rStream)
    print(f"(child <--- parent) : {rStream_fo.read()}")
    os.close(child_rStream)
