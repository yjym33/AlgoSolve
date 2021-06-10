# https://www.acmicpc.net/problem/13305

n = int(input())
roads = list(map(int, input()))
costs = list(map(int, input()))

res = 0
m = costs[0]
for i in range(n-1):
    if costs[i] < m:
        m = costs[i]
    res += m * roads[i]

print(res)

# 1. 도시의 기름값 배열을 탐색하며 현재 최저값 보다 더 작은 값이 나오면 갱신하면서 풀어가면 된다.
# 2. 첫 도시의 기름값을 m으로 두고, roads를 탐색하며 같은 위치의 도시의 기름값이 더 작으면 그 값을 m으로 바꾸고, 도로 길이를 곱한 값을 sum에 더한다.