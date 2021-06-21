# 문제 출처 : https://www.acmicpc.net/problem/20115

N = int(input())
Drink = list(map(int, input().split()))
Drink.sort(reverse=True)
sum_Drink = Drink[0]

for i in range(1, N):
    sum_Drink += Drink[i]/2
print(sum_Drink)


