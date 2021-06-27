a = list(range(21))n # 총 카드의 개수 리스트
for _ in range(10): # 10개의 범위가 주어짐
    s, e = map(int, input().split()) # 10개의 범위의 시작과 끝점
    for i in range((e-s+1)//2): 
        a[s+i], a[e-i] = a[e-i], a[s+i]
        print(a)
a.pop(0)
for x in a:
    print(x, end=' ')
