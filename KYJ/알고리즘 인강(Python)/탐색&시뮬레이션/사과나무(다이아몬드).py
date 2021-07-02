n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
res=0
s=e=n//2
for i in range(n):
    # s부터 e까지 돌기
    for j in range(s,e+1):
        res+=a[i][j]
    # i가 n//2보다 작아질 때
    if i<n//2:
        # 시작점은 한칸을 빼고, 끝점은 한칸을 늘린다.
        s-=1
        e+=1
    # i가 n//2보다 클 때
    else:
        # 시작점을 한칸을 늘리고, 끝점을 한칸씩 줄인다.
        s+=1
        e-=1
print(res)
