# https://www.acmicpc.net/problem/2217

# 풀이 1

# N = int(input())

# rope = []
# value = []

# for i in range(N):
#     rope.append(int(input()))
# rope.sort(reverse=True)  # 1
# for num in range(N):
#     value.append(rope[num] * (num+1))  # 2

# print(max(value))

# 풀이 2

def solution():
    arr.sort(reverse=True) # 내림차순으로 정렬
    for i in range(N):
        arr[i] = arr[i] * (i + 1)

    return max(arr) # 계산한 값중 가장 큰값을 리턴

N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

print(solution())

# 문제 풀이

# 로프를 병렬로 연결하면 각 로프에는 w/k 만큼 동일한 중량이 걸린다.
# 즉, 가장 작은 무게를 들수 있는 로프가 들수 있는 질량 * 병렬 로프 연결 개수 = 최종 무게
# 먼저 가장 무거운 무게를 들수 있는 로프부터 내림차순으로 정렬을 한다.
# 예를 들어 30 40 50 60 70의 무게가 있다고 한다면 이를 내림차순으로 정렬하면 [70,60,50,40,30]이 된다.
# 그 이후에 1부터 N까지 가장 큰 수부터 곱해준다.
# [70*1, 60*2, 50*3, 40*4, 30*5] 여기서 가장 큰 값이 답이므로 40*4 = 160이 답이 된다.