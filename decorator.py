def decorator(fun):
    def wrapper(arg):
        res = 1 + arg
        print(res)
        print('func', fun.__name__)
        print(fun(2))
    return wrapper


@decorator
def example_fun(a: int) -> int:
    return a + 2


example_fun(2)
