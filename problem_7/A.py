import os

readStream, writeStream = os.pipe()

#create child process
pid = os.fork()

#parent process
if pid > 0:
    os.close(readStream)    # A single process can only open a single file descriptor
    print("Parent --------(pipe)--------> Child")
    text = b"parent to child process info"
    os.write(writeStream, text)
    print(f"sent to child : {text.decode()}\n\n")

else:
    os.close(writeStream)
    print("Child <-------(pipe)---------Parent" )
    readStream_fo = os.fdopen(readStream)   # Opening a file object from a file descriptor.
    print(f"from parent: {readStream_fo.read()}")
