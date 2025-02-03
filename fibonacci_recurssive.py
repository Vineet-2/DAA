import time

def fib_rec(num):
    if num<=1:
        return num
    else:
        return fib_rec(num-2) + fib_rec(num-1)

num=40

start=time.perf_counter()
fibonacc_rec=fib_rec(num)
end=time.perf_counter()

print(f"The {num} Term of Fibonacci is: {fibonacc_rec}")
print(f"Time Taken by Recursive Approach: {end-start}s")