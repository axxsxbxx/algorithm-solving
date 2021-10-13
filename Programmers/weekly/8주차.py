 def solution(sizes):
    cards = []
    for a, b in sizes:
        if a > b:
            cards.append([a, b])
        else:
            cards.append([b, a])
    
    max_a = max([c[0] for c in cards])
    max_b = max([c[1] for c in cards])
    
    return max_a * max_b