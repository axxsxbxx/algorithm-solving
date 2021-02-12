while True:
    num = int(input())
    if num == -1:
        break
    numbers = []
    for i in range(1, num):
        if num % i == 0:
            numbers.append(i)
    
    if num == sum(numbers):
        print('{} = '.format(num), end='')
        for i in range(len(numbers)-1):
            print('{}'.format(numbers[i]), end=' + ')
        print('{}'.format(numbers[-1]))
    else:
        print('{} is NOT perfect.'.format(num))