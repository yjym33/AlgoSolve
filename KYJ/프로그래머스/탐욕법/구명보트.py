# 문제

# 무인도에 갇힌 사람들을 구명보트를 이용하여 구출하려고 합니다. 구명보트는 작아서 한 번에 최대 2명씩 밖에 탈 수 없고, 무게 제한도 있습니다.
# 예를 들어, 사람들의 몸무게가 [70kg, 50kg, 80kg, 50kg]이고 구명보트의 무게 제한이 100kg이라면 2번째 사람과 4번째 사람은 같이 탈 수 있지만 
# 1번째 사람과 3번째 사람의 무게의 합은 150kg이므로 구명보트의 무게 제한을 초과하여 같이 탈 수 없습니다.
# 구명보트를 최대한 적게 사용하여 모든 사람을 구출하려고 합니다.
# 사람들의 몸무게를 담은 배열 people과 구명보트의 무게 제한 limit가 매개변수로 주어질 때, 
# 모든 사람을 구출하기 위해 필요한 구명보트 개수의 최솟값을 return 하도록 solution 함수를 작성해주세요.

# 제한사항

# 무인도에 갇힌 사람은 1명 이상 50,000명 이하입니다.
# 각 사람의 몸무게는 40kg 이상 240kg 이하입니다.
# 구명보트의 무게 제한은 40kg 이상 240kg 이하입니다.
# 구명보트의 무게 제한은 항상 사람들의 몸무게 중 최댓값보다 크게 주어지므로 사람들을 구출할 수 없는 경우는 없습니다.

# 입출력 예
# people	            limit	    return
# [70, 50, 80, 50]	    100	           3
# [70, 80, 50]	        100	           3


# 문제 풀이 방법 (이분탐색)

# 1. 오름차순 정렬한다.
# 2. start, end = 0, len(people)-1 지정하여 가장 가벼운 사람 가장 무거운 사람을 지정한다. 
# 3. people[start] + pelple[end] <= limit 이면 2명이서 보트를 탈수 있으므로, start와 end를 변경할수 있다.
# 4. 사람 수는 최대로 필요한 보트 수를 의미하므로 "사람의 수 - 이분 탐색을 통해 구한 값"을 하면 원하는 답을 얻을 수 있다.


def solution(people, limit):
    answer = 0
    people.sort()
    
    start ,end = 0, len(people) - 1
    
    while start < end:
        if people[start] + people[end] <= limit: 
            start += 1
            answer += 1
        end -= 1
        
    return len(people) - answer

# 디버깅 (예시기준)

# answer : 0   people.sort : [50, 50, 70, 80], start = 0 end = len(people) - 1
# start < end: 0 < 3,   people[start] = 50 + people[end] = 80 <= limit : 100 >> 50 + 80 <= 100 false
# end -= 1 이므로 2 다시 start < end: >> 0 < 2: >> 50 + 70 <= 100 false
# end -= 1 이므로 1 다시 start < end: >> 0 < 1: >> 50 + 50 <= 100 true
# start = 1 answer = 1 다시 while문 돌아가서 진행 start < end: >> 1 < 1: 이므로 조건 만족 안하므로 while문 빠져나옴
# return 문 len(people) - answer  = 4 -1 = 3 


