# 문제 링크 : https://www.acmicpc.net/problem/2231

n = int(input())
result = 0
for i in range(1, n+1):
    a = list(map(int, str(i))) # 각 자리수를 분해한다.
    s = i + sum(a) # 분해합을 구한다. 
    if (s == n): # 만약 분해합이 n과 같다면
        result = i # x = i 이므로 종료
        break
print(result)