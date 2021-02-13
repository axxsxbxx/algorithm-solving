n = int(input())
num = n
cnt = 0

while True:
    num_sum = num//10 + num%10
    
    if num_sum < 10:
        new_num = num_sum + (num%10)*10
    else:
        new_num = (num%10)*10 + num_sum%10
    
    cnt += 1
    num = new_num
    
    if new_num == n:
        break

print(cnt)