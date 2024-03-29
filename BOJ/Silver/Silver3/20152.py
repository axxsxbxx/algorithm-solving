'''
20152. Game Addiction

강산이는 심각한 게임 중독자이기 때문에 날씨에 상관없이 매일 PC방을 간다.
최근에 폭우로 인해 일부 지역이 침수되어 침수된 지역으로는 이동할 수 없게 되었다. 하지만 강산이는 출석 이벤트를 위해 하루도 빠짐없이 PC방을 가야 한다.
강산이는 PC방까지 상, 하, 좌, 우 방향으로만 이동하며, 한 번 이동할 때의 거리는 1이다. 또한, 강산이는 게임을 빨리하러 가야 하기 때문에 집에서 PC방까지 최단경로로 움직인다.
강산이의 집의 좌표 (H, H)와 PC방의 좌표 (N, N)이 주어지고 좌표평면 위 (x, y)에서 y > x인 곳은 침수되었다고 할 때, 강산이가 침수된 지역을 피해서 PC방까지 갈 수 있는 경로의 개수를 구하라.
단, PC방의 좌표가 집의 좌표 같은 경우 경로는 1가지라고 한다.

입력
첫째 줄에 집과 PC방의 좌표 (H, H), (N, N) 을 나타내는 두 정수 H, N (0 ≤ H, N ≤ 30) 이 차례로 주어진다.

출력
집에서 PC방까지 갈 수 있는 경로의 개수를 출력한다.
'''
H, N = map(int, input().split())


'''
[입력]
8 4

[출력]
14
'''