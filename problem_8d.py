import threading
import random
import time


class PetersonSolution():
    other = 1
    turn = 0

    interested = [False, False]

    def EntrySection(self, *args):
        # if process 0 entered other process would be 1 and if process 1 entered other process would be 0.
        PetersonSolution.other = 1 - args[0]
        # entered process is intrested, hence True
        PetersonSolution.interested[args[0]] = True

        # set turn to the entering process
        PetersonSolution.turn = args[0]

        # if other process is already in the critical section prevent any other process from entering
        while PetersonSolution.interested[PetersonSolution.other] == True and PetersonSolution.turn == args[0]:
            print(f"Process {args[0]} is waiting")

        # if no process is in critical section then run critical  section
        print(f"Process {args[0]} Entered Critical Section")

        self.ExitSection(args[0])
        time.sleep(3000)

    def ExitSection(self, process):
        PetersonSolution.interested[process] = False

    def main(self):
        i = 0
        while i < 100:
            i+=1
            t1 = threading.Thread(target=self.EntrySection, args=(0,))
            t1.start()
            t2 = threading.Thread(target=self.EntrySection, args=(1,))
            t2.start()


if __name__ == "__main__":
    p = PetersonSolution()
    p.main()