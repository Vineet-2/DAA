import time

def fib_bottom_up(num):
    table=[0]*(num + 1)
    if num<=1:
        return num
    else:
        table[1]=1
        for i in range(2,num+1):
            table[i]=table[i-2]+table[i-1]
    return table[num]

num=100

start=time.perf_counter_ns()
fibonacci_bottom_up=fib_bottom_up(num)
end=time.perf_counter_ns()

print(f"The {num} Term of Fibonacci is: {fibonacci_bottom_up}")
print(f"Time Taken by Bottom Up Approach: {end-start}ns")

