from collections import defaultdict

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    
    report_cnt = defaultdict(int)
    report_person = defaultdict(list)
    result_mail = defaultdict(int)
    
    real_report = set(report)
    
    for r in real_report:
        a, b = r.split()
        report_cnt[b] += 1
        report_person[a].append(b)
    
    stop_id = []
    
    # 정지된 ID 체크
    for id in id_list:
        if(report_cnt[id] >= k):
            stop_id.append(id)
        
    # 처리 결과 메일 수신 횟수 구하기
    i = 0
    for id in id_list:
        for person in report_person[id]:
            if person in stop_id:
                answer[i] += 1
        i += 1
    return answer