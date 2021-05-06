def solution(scoville, K):
    import heapq
    answer = 0

    heapq.heapify(scoville) # 리스트를 heap 자료형으로 변환

    while scoville:
        first = heapq.heappop(scoville) # heap에서 가장 작은 원소를 꺼냄

        if first >= K:
            break

        if len(scoville) <= 0:
            return -1
        
        second = heapq.heappop(scoville) # heap에서 두번쨰로 작은 원소 꺼냄
        heapq.heappush(scoville, first + second * 2) 
        # first + second * 2를 scoville에 추가
        answer += 1
    
    return answer