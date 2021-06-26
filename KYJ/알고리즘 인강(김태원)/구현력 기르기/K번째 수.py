T = int(input()) # 테스트 케이스가 주어진다.
for t in range(T): # 테스트케이스가 주어졌으므로 각 테스트케이스 별로 반복문을 돈다.
    n, s, e, k = map(int,input().split()) # n, s, e, k 가 주어진다.
    a = list(map(int, input().split()) # N개의 숫자가 주어진다.
    a = a[s-1:e] # s번째부터 e번째 까지의 숫자를 오름차순으로 정렬해야하므로 선택한다.
    a.sort() # 오름차순 정렬
    print(a[k-1]) # k번째 수 출력

