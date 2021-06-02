import ctypes
import pathlib

fact_lib = ctypes.CDLL("./source/factorial/libs/A.so")

prime_lib = ctypes.CDLL("./source/prime/libs/B.so")
prime_lib.isPrime.restype = ctypes.c_bool

print(fact_lib.findFactorial(10))
print(prime_lib.isPrime(1))