import time

def fibonacci_seq_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def prime_num_getter(n):
    primes = []
    generator = fibonacci_seq_generator()
    while len(primes) < n:
        num = next(generator)
        if num > 1 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            primes.append(num)
    print(f"Перші {n} простих чисел з послідовності Фібоначі: {primes}")


def timer_wrapper(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Час виконання функції: {end_time - start_time:.6f} секунд")
        return result
    return wrapper


@timer_wrapper
def get_prime_numbers(n):
    prime_num_getter(n)


get_prime_numbers(10)
