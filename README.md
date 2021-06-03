# EIS assignment

## Problem 1:
Write a program which will create n process. show that the processes will run asynchronously on CPU (i.e. there is no specific order in which the process are scheduled on the CPU).

![answer1.png](res/1.png)

<br>

## Problem 2:
Demonstrate the Creation of a Zombie process and also show that the zombie process can be prevented.

### A) Zombie process created:
![answer2a.png](res/2a.png)

<br>

### B) Zombie process is prevented:
![answer2b.png](res/2b.png)

<br>

## Problem 3:
Write a program which creates, say 10 process. Let them run in an infinite loop. show that the processes are scheduled on the CPU in no specific order.

![answer3.png](res/3.png)

<br>

## Problem 4:
Show that a user level thread blocks the entire process when it calls a blocking system call.

![answer4.png](res/4.png)

<br>

## Problem 5:
Give a solution to the bounded buffer producer and consumer problem using semaphore. The buffer should implement in a shared memory. Producer and consumer should be two distinct processes. The buffer state at different times should be captured in a text file or in a graphical representation.

![answer5.png](res/5.png)

<br>

## Problem 6:
Create two shared libraries A.so (contains the function definition of factorial) and B.so (containing the function ifprime). Link these libraries dynamically to your executable where factorial and ifprime function is used and demonstrate that a shared library is loaded into memory only when dlopen is called and offloaded from memory when dlclose called for that library. Also, do the same as above creating archives libraries A.a and B.a. Show that the size of executable in this case more than the size of executable in the earlier case. 

### A) Dynamically linked the libraries (.so) to the main program:
![answer6a.png](res/6a.png)

<br>

### B) Built executable using the archive libraries (.a) made from individual libraries:
![answer6b.png](res/6b.png)

<br>

## Problem 7:
### A) Create a pipe between a parent and its child and send data down the pipe. With proper example.
![answer7a.png](res/7a.png)

<br>

### B) Create two pipes before the fork, to implement interprocess communication between parent and child.
![answer7b.png](res/7b.png)

<br>

### C) Implement an IPC (or two half-duplex pipes), such that the coprocess add2 is invoked when two numbers are read from standard input and the value from the co-process is written to its standard output.
![answer7c.png](res/7c.png)