''' Use Yield to get FIbonacci Nums '''


def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b


def generate_fib_nums(n : int = 30):
    fibgen = fibonacci_generator()
    if n <=0 :
        return 0
    elif n ==1 :
        return 1
    else:
        for _ in range(n):
            fibnum = next(fibgen)
    return fibnum

if __name__ == "__main__":
    print(generate_fib_nums(n=20))