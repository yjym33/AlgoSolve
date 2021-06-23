# 문제 출처 : https://www.acmicpc.net/problem/11047

n, k = map(int, input().split())
coins = []

for i in range(n):
    coins.append(int(input()))
result = 0

coins = coins[::-1] # 내림차순으로 정렬한다.
for i in range(n):
    if k // coins[i] > 0: # 나눌수 있다면
        result += k // coins[i] # 나누어 발생한 몫 / 동전의 개수
        k = k % coins[i] # 나머지를 다시 for문으로 계속 나눈다.
print(result)

# 그리디 알고리즘으로 푸는 문제이다.
# 동전의 개수를 최소로 만들기 위해서는 동전의 액수를 내림차순으로 나눌수 있는 가장 큰 수부터 나누면 된다.
# 이 문제는 나누어 떨어지는 조건이 없기 떄문에 간단하다.

