import os
import multiprocessing

c_rS, p_wS = os.pipe()
p_rS, c_wS = os.pipe()


def add2():
    os.close(p_wS)
    os.close(p_rS)

    rS_fo = os.fdopen(c_rS)
    res = str(rS_fo.read())
    os.close(c_rS)

    print("\nEntering add2 process........")

    num1, num2 = map(int, res.split(" "))
    ans = f"{num1} + {num2} = {num1 + num2}".encode()

    print(
        "Exiting add2 process and sending result to the main process.......\n")

    os.write(c_wS, ans)
    os.close(c_wS)


add2_process = multiprocessing.Process(target=add2)
add2_process.start()

os.close(c_wS)
os.close(c_rS)

nums = input("Enter two numbers: ")

os.write(p_wS, nums.encode())
os.close(p_wS)

rS_fo = os.fdopen(p_rS)
res = str(rS_fo.read())
os.close(p_rS)

print(res)