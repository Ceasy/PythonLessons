task = open('todos.txt', 'r')
print('evelina, 1.', file=task)
print('mandarin 2.', file=task)
print('frosya 3', file=task)

for i in task:
    print(i)
task.close()