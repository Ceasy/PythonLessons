def a_fun():
    #Обычная ф-ция.
    return '1 + 1'


if __name__ == '__main__':
    value_a = a_fun()
    print(value_a)




def another_fun(fun):
    def b_fun():
        value_b = 'Результат от %s это %s' % fun(), eval(fun())
        return value_b

    return b_fun()