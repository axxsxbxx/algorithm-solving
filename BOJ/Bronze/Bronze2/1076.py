'''
1076. 저항

전자 제품에는 저항이 들어간다. 저항은 색 3개를 이용해서 그 저항이 몇 옴인지 나타낸다.
처음 색 2개는 저항의 값이고, 마지막 색은 곱해야 하는 값이다.
'''
colors = ['black', 'brown', 'red', 'orange', 'yellow',
        'green', 'blue', 'violet', 'grey', 'white']

color = dict(zip(colors, range(10)))

c1 = input()
c2 = input()
c3 = input()

num = color[c1]*10 + color[c2]
result = num * (10**color[c3])
print(result)
'''
[입력]
yellow
violet
red

[출력]
4700
'''