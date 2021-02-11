h, m = map(int, input().split())
cook = int(input())
hour = h + cook // 60
minute = m + cook % 60

if minute > 59:
    hour += 1
    minute = minute - 59 - 1
if hour > 23:
    hour = hour % 24
    
print('{} {}'.format(hour, minute))
