def double(arg):
    print('Before:', arg)
    arg = arg * 2
    print('After: ', arg)


def change(arg):
    print('Before: ', arg)
    arg.append('More data')
    print('After: ', arg)


num = [1,2,3,4]
change(num)
print(num)

########################################
"""listText = []

for i in range(99):
    entTxt = input('Pls, enter arg in txt, (or enter "exit" for exit in program): ')
    if entTxt != 'exit':
        listText.append(entTxt)
        print('i: ', i)
    else:
        print(listText)
        break
"""