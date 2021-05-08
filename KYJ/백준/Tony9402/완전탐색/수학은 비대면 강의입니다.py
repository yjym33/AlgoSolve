# 문제 링크 : https://www.acmicpc.net/problem/19532

a, b, c, d, e, f = map(int, input().split())
for i in range(-999, 1000): # 문제의 범위를 주었기 떄문에 이를 만족하는 범위를 지정한다.
    for j in range(-999, 1000):
        if (a*i)+(b*j) == c and (d*i)+(e*j) == f:
            print(i,j)