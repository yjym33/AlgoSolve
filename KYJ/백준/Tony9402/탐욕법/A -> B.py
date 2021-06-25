# 문제 출처 : https://www.acmicpc.net/problem/16953

import sys

A, B = map(int, sys.stdin.readline().split())

count = 1

while True:
    if A == B:
        break
    elif A > B or (B% 10 != 1 and B % 2 != 0):
        count = -1
        break
    elif B % 10 == 1:
        B //= 10
        count += 1
    elif B % 2 == 0:
        B //= 2
        count += 1

print(count)

# 이 문제는 거꾸로 B에서 A를 만들어 내는 방법으로 푸는 것이 효율적이다.
# B에서 10을 나눠서 나머지가 1이면 다음 B는 몫이 됩니다.