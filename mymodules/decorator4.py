def decorator(fun):
    def wrapper(arg_1, arg_2):
        print('Hello! function name is', fun.__name__ + '()', 'and Argument a = ', arg_1, ', Argument b = ', arg_2)
        fun(arg_1, arg_2)

    return wrapper


@decorator
def fun_example(arg_a: int, arg_b: int):
    print('TOTAL = ', arg_a + arg_b)


fun_example(int(input('please enter arg 1: ')), int(input('please enter arg 2: ')))
