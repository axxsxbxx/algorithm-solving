'''
2056. 연월일 달력

연월일 순으로 구성된 8자리의 날짜가 입력으로 주어진다.
해당 날짜의 유효성을 판단한 후, 날짜가 유효하다면
”YYYY/MM/DD”형식으로 출력하고,
날짜가 유효하지 않을 경우, -1 을 출력하는 프로그램을 작성하라.
'''
t = int(input())
test_case = []

for _ in range(t):
    test_case.append(input())
i = 1
for date in test_case:
    month = int(date[4:6])
    day = int(date[6:8])

    if month < 1 or month > 12:
        print(f'#{i} -1')
        i += 1
        continue
    elif month in (1, 3, 5, 7, 8, 10, 12):
        if day < 1 or day > 31:
            print(f'#{i} -1')
            i += 1
            continue
    elif month in (4, 6, 9, 11):
        if day < 1 or day > 30:
            print(f'#{i} -1')
            i += 1
            continue
    elif month == 2:
        if day < 1 or day > 28:
            print(f'#{i} -1')
            i += 1
            continue

    print(f'#{i} {date[:4]}/{date[4:6]}/{date[6:]}')
    i += 1
        
'''
[입력]
5
22220228
20150002
01010101
20140230
11111111

[출력]
#1 2222/02/28
#2 -1
#3 0101/01/01
#4 -1
#5 1111/11/11
'''