h, m, s = map(int, input().split())
time = int(input())

hour = h + time // 3600
time %= 3600

minute = m + time // 60
time %= 60

second = s + time

if second > 59:
    minute += 1
    second = second - 59 -1
if minute > 59:
    hour += 1
    minute = minute - 59 - 1
if hour > 23:
    hour = hour % 24
    
print('{} {} {}'.format(hour, minute, second))