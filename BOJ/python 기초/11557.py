T = int(input())

for _ in range(T):
    n = int(input())
    univ = []
    drink = []
    for _ in range(n):
        a, b = input().split()
        univ.append(a)
        drink.append(int(b))
    max_idx = 0
    max_num = 0
    for i in range(len(drink)):
        if drink[i] > max_num:
            max_num = drink[i]
            max_idx = i
    print(univ[max_idx])