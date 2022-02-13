def solution(lottos, win_nums):
    rank_dict = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    
    # 최저 순위는 현재 일치하는 것만 일치하는 경우
    cnt = 0
    for num in lottos:
        if num in win_nums:
            cnt += 1
    low_rank = rank_dict[cnt]
    
    # 최고 순위는 현재 일치하는 것 + 0으로 표기된 게 모두 일치하는 경우
    cnt += lottos.count(0)
    high_rank = rank_dict[cnt]
    
    return [high_rank, low_rank]