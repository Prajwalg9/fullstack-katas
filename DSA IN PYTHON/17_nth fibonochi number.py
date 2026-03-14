import time

n = int(input('Enter index (keep it under 6!): '))


def fibonacci(n):
    print(f"Checking fibonacci({n})...")

    if n == 0 or n == 1:
        print(f"--> Base case hit! Returning {n}")
        return n
    else:
        print(f"--> Splitting into fibonacci({n - 1}) and fibonacci({n - 2})")
        return fibonacci(n - 1) + fibonacci(n - 2)


start_time = time.perf_counter()
result = fibonacci(n)
end_time = time.perf_counter()

print(f"\nFinal Result: {result}")
print(f"Execution Time: {end_time - start_time:.6f} seconds")