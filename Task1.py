def fibonacci_seq_generator():
    a = 0
    b = 1

    while True:
        yield a
        t = a
        a = b
        b = t + b

generator = fibonacci_seq_generator()

for i in range(1, 11):
    print(next(generator))