def solution(n, costs):
    
    def find_set(x):
        if x != island[x]:
            island[x] = find_set(island[x])
        return island[x]
    
    costs.sort(key=lambda x:x[2])
    island = list(range(n))
    ans = 0

    for s, e, w in costs:
        start, end = find_set(s), find_set(e)
        if start != end:
            island[end] = start
            ans += w
            
    return ans