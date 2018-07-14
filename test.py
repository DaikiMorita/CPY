import fibonacci
import time

def fibonacci_n(n):

	if n < 2:
		return 1
	else:
		return fibonacci_n(n-1) + fibonacci_n(n -2)

NUM = 40

print("c module")

start = time.time()

r = [fibonacci.fibonacci(n) for n in range(NUM)]

elapsed_time_f = time.time() - start

print(elapsed_time_f)
print(r)

print("native python")

start = time.time()

r = [fibonacci_n(n) for n in range(NUM)]

elapsed_time_n = time.time() - start

print(elapsed_time_n)
print(r)


print("Result")
print( float(elapsed_time_n / elapsed_time_f))


