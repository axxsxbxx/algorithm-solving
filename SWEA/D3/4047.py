'''
4047. 영준이의 카드 카운팅

최근 영준이는 카드 게임에 꽂혀 있다.
영준이가 하는 카드 게임에는 한 덱의 카드가 필요한데 
여기서 얘기하는 “한 덱”이란 스페이드, 다이아몬드, 하트, 클로버 무늬 별로 각각 A, 2~10, J, Q, K의 라벨 즉 4개의 무늬 별로
각각 13장씩 총 52장의 카드가 있는 모음을 의미한다.
편의상 A는 1, J, Q, K는 11, 12, 13으로 하여 1~13의 숫자가 카드에 적혀있다고 하자.
영준이는 몇 장의 카드를 이미 가지고 있는데 게임을 하기 위해서 몇 장의 카드가 더 필요한지 알고 싶어 한다.
그리고 이미 겹치는 카드를 가지고 있다면 오류를 출력하고자 한다.
지금 가지고 있는 카드의 정보가 주어지면 이 작업을 수행하는 프로그램을 작성하라.
'''
def get_result(cards):
    deck = {'S': [0]*13, 'D': [0]*13, 'H': [0]*13, 'C': [0]*13}
    # 해당 카드가 존재하는 경우 카운트
    for i in range(0, len(cards), 3):
        deck.get(cards[i])[int(cards[i+1:i+3])-1] += 1
    # 만약 딕셔너리 값이 1보다 큰 경우 ERROR 리턴
    for num in deck.values():
        for n in num:
            if n > 1:
                return 'ERROR'
    # 이렇게 명시해주지 않으면 딕셔너리기 때문에 실행할때마다 결과 바뀜
    result = [13 - sum(deck['S']),
              13 - sum(deck['D']),
              13 - sum(deck['H']),
              13 - sum(deck['C'])]
    return result

T = int(input())
for t in range(1, T+1):
    c = input()
    ans = get_result(c)
    if ans == 'ERROR':
        print('#%d %s' % (t, ans))
    else:
        s, d, h, c = ans
        print('#%d %d %d %d %d' % (t, s, d, h, c))

'''
[입력]
3
S01D02H03H04
H02H10S11H02
S10D10H10C01

[출력]
#1 12 12 11 13
#2 ERROR
#3 12 12 12 12 
'''