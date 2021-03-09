'''
2007. 패턴 마디의 길이

패턴에서 반복되는 부분을 마디라고 부른다. 
문자열을 입력 받아 마디의 길이를 출력하는 프로그램을 작성하라.
'''
T = int(input())
for t in range(1, T+1):
    pattern = input()
    min_num = 987654321
    for i in range(1, 10):
        base = pattern[:i]
        if base == pattern[i:i*2]:
            if len(base) < min_num:
                min_num = len(base)
    print('#%d %d' % (t, min_num))
'''
[입력]
3
KOREAKOREAKOREAKOREAKOREAKOREA
SAMSUNGSAMSUNGSAMSUNGSAMSUNGSA
GALAXYGALAXYGALAXYGALAXYGALAXY

[출력]
#1 5
#2 7
#3 6
'''