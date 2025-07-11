https://www.acmicpc.net/problem/1463

n = int(input())
d = [0] * 1000001
for i in range(2, n+1): # d[1] = 0 이므로 d[2]부터 시작해야함
    # 1을 빼는 경우
    d[i] = d[i-1] + 1
    # 2를 나누는 경우
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)
    # 3을 나누는 경우
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)
print(d[n])

# 이 문제의 핵심은 각 숫자에서 소요되는 최소수는 이전 단계에서 + 1을 하면 성립한다는 것이다.
# ex) 10 -> 5 -> 4 -> 2 -> 1, 10 -> 9 -> 3 -> 1
#     d[10] = 4, d[5] = 3, d[4] = 2, d[2] = 1, d[1] = 0
# 즉 d[10] = d[5] + 1 , d[5] = d[4] + 1, d[4] = d[2] + 1 , d[2] = d[1] + 1
# 점화식 : dp[N] = min(dp[N-1], dp[N//2], dp[N//3]) + 1