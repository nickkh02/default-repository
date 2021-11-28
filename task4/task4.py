import sys

with open(sys.argv[1], 'r') as f:
    nums = [int(line) for line in f]

def counter(array, num):
    n = array[num]
    c = 0
    i = 0
    for i, item in enumerate(array):
        if array[i] != n:
            if array[i] > n:
                c += array[i] - n
            elif array[i] < n:
                c += n - array[i]
            else:
                pass
    return c

def rounder(array):
    list_of_steps = []
    for i in range(len(array)):
        list_of_steps.append(counter(array, i))
    return(min(list_of_steps))

print('Минимальное количество ходов:', rounder(nums))
