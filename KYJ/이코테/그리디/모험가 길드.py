N = int(input())

data = list(map(int, input().split()))
data.sort()  # 오름차순 정렬

group = 0 # 총 그룹의 수
count = 0 # 그룹에 속한 모험가의 수

for i in data:
    count += 1

    if count >= i:
        group += 1
        count = 0

print(group)



# 생각 순서도 

# 모험가의 수, 모험가의 공포도 값을 입력 받는다 -> 공포도를 오름차순으로 정렬 ->  작은 순서부터 그룹에 포함될 모험가의 수를 확인 -> 모험가의 수가 현재 공포도 이상이면 그룹 결성

# 예시 : 2 3 1 2 2  -> 1 2 2 2 3 -> 1 / 2 2 / 2 3 (세명이 되지 못하므로 그룹 결성 X) 따라서 출력 2 (두개의 그룹)