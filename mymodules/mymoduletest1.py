def decorator(fun):
    def wrapper(arg_a: int, arg_b: int) -> 'function':
        """After function example"""
        print(fun(arg_a, arg_b))
        """Before function example"""
        print(arg_a + arg_b)

    return wrapper


@decorator
def subtraction(a: int, b: int) -> int:
    return a - b

#Functions for myTestWeb module
def sum_num(a: int, b: int) -> int:
    return a + b

def sum_function(a: float, b: float, act: str) -> float:
    if act == '+':
        return  a + b
    elif act == '-':
        return a - b
    elif act == '*':
        return a * b
    elif act == '/':
        return a / b
    else:
        return -991