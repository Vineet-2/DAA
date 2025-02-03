import time

def fib_top_down(num, memo={}):
    if num <=1:
        return num
    else:
        if num not in memo:
            memo[num] = fib_top_down(num - 1) + fib_top_down(num - 2)
    return memo[num]

num=100

start=time.perf_counter_ns()
fibonacc_top_down=fib_top_down(num)
end=time.perf_counter_ns()

print(f"The {num} Term of Fibonacci is: {fibonacc_top_down}")
print(f"Time Taken by Top Down Approach: {end-start}ns")
