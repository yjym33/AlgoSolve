n = int(input())
res = 0

for i in range(n):
    tmp = input().split()
    tmp.sort()
    a, b, c = map(int, tmp)
    if a==b and b==c: # 3개가 다 같은경우
        money = 10000 + a * 1000;
    elif a==b or a==c: # 2개가 같은 경우
        money = 1000 + (a * 100)
    elif b==c:
        money = 1000 + (b * 100)
    else:
        money = c * 100

    if money > res:
        res = money

print(res)


