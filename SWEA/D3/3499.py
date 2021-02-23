'''
3499. 퍼펙트 셔플

카드를 퍼펙트 셔플 한다는 것은, 카드 덱을 정확히 절반으로 나누고 
나눈 것들에서 교대로 카드를 뽑아 새로운 덱을 만드는 것을 의미한다.
N개의 카드가 있는 덱이 주어질 때 이를 퍼펙트 셔플하면 어떤 순서가 되는지 출력하는 프로그램을 작성하라.
만약 N이 홀수이면, 교대로 놓을 때 먼저 놓는 쪽에 한 장이 더 들어가게 하면 된다. 
'''
def perfect_shuffle(n, deck):
    result = []
    k = (n+1)//2

    first = deck[:k]
    second = deck[k:]

    for i in range(len(second)):
        result.append(first[i])
        result.append(second[i])

    if n % 2:
        result.append(first[-1])
    return result


T = int(input())
for t in range(1, T+1):
    N = int(input())
    cards = input().split()
    ans = perfect_shuffle(N, cards)
    print('#%d %s' % (t, ' '.join(ans)))

# 다른 방법 (리스트 추가적으로 사용하지 않는 방식)
# j = (n+1) // 2
# for i in range(j):
#     print(lst[i], end=' ')
#     if j < N:
#         print(lst[j], end=' ')
#         j += 1
'''
[입력]
3
6
A B C D E F
4
JACK QUEEN KING ACE
5
ALAKIR ALEXSTRASZA DR-BOOM LORD-JARAXXUS AVIANA	

[출력]
#1 A D B E C F
#2 JACK KING QUEEN ACE
#3 ALAKIR LORD-JARAXXUS ALEXSTRASZA AVIANA DR-BOOM
'''