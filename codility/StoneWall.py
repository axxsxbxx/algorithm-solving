# O(N)
def solution(H):
    blocks = 0
    wall = []

    for h in H:
        # 높이가 낮아질 경우
        while len(wall) > 0 and h < wall[-1]:
            wall.pop()
        
        # 높이가 높아질 경우 or wall이 비어있는 경우...?
        if len(wall) == 0 or h > wall[-1]:
            blocks += 1
            wall.append(h)

    return blocks
