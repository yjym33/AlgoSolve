# 문제 출처 : https://www.acmicpc.net/problem/13164


N, K = map(int, input().split())
person = list(map(int, input().split()))

dp = []
for i in range(N-1):
    dp.append(person[i+1] - person[i])
dp.sort()

answer = 0
for i in range(N-K):
    answer += dp[i]
print(answer)



# 그룹을 만들어 그룹내의 키차이가 최소가 되도록 모든 그룹의 키차이를 구하는 문제

# N명의 학생들을 K개의 그룹으로 나눈다고 할떄 이 말을 다르게 한다면, N-K 개의 키 차이를 무시할수 있다는 것이다.