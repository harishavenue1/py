# infinite fibonacci series
def fibonacci(a, b):
    print(a, end=",")
    while True:
        b, a = a + b, b
        fibonacci(a, b)


fibonacci(5, 6)
