n = int(input())
a = list(map(int, input().split()))
ave = round(sum(a))
min = 214700000
for idx, x in enumerate(a):
    tmp = abs(x-ave)
    if tmp < min:
        min = tmp
        score = x
        res = idx + 1
    elif tmp == min:
        if x > score:
            score = x
            res = idx + 1
print(ave, res)