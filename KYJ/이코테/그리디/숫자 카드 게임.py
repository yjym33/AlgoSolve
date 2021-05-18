N, M = map(int, input().split())

result = 0

for i in range(N):
    Data = list(map, int(input().split()))

    min_number = min(Data)

    result = max(result, min_number)

print(result)

# 이 문제의 아이디어는 "각 행마다 가장 작은 수를 찾은 후에 그 수중에서 가장 큰 수를 찾는 것이다."

# 배열에서 가장 작은 수를 찾는 방법을 이용하여 각 행에서 가장 작은 수를 찾은후, 그중에서 가장 큰 수를 찾는 방법이다.

# 필요 함수 : min()

# 풀이 순서도 : 

# 행의 개수, 열의 개수 입력받기 -> 값을 담을 result 선언 -> 한 줄씩 데이터를 입력받음 -> 현재 줄에서 가장 작은수 찾기 -> 가장 작은 수 중에서 가장 큰수 찾기