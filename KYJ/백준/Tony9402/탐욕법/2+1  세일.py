#  문제 출처 : https://www.acmicpc.net/problem/11508

n = int(input())

cost = [] # 유제품 가격 리스트
for i in range(n):
    a = int(input())
    cost.append(a)
cost.sort(reverse=True)

count = 1 # 리스트 안의 순서를 세주는 count 값 1로 지정
result = 0
for i in cost:
    if cost%3 != 0:
        result += i
        count += 1
    else: # 만약 리스트 원소가 3의 배수 자리에 있다면 result에 원소값을 더해주지 않는다.
        count += 1
print(result)

# 이 문제의 핵심은 "내림차순으로 정렬한 후 3의 배수 자리를 없애주는 것이다."

