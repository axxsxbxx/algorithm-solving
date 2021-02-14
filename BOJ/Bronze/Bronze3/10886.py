n = int(input())
cute = 0
no_cute = 0
for _ in range(n):
    num = input()
    if num == '1':
        cute += 1
    else:
        no_cute += 1
        
if cute > no_cute:
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')