def param_transfer(fun):
    def wrapper(arg):
        print('Run function: ' + str(fun.__name__) + '(), with param: ' + str(arg))
        fun(arg)
        print('omg')
    return wrapper


@param_transfer
def print_sqrt(num):
    print(num**0.5)


print_sqrt(int(input('pls, enter num: ')))

