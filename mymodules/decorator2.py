def decorator1(func):
    def wrapper():
        print('Code 1')
        func()
        print('Code 2')
    return wrapper


@decorator1
def singl_fun():
    print('Code single')

rename_func = singl_fun
rename_func()