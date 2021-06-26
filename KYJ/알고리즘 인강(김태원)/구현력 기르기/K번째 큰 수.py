N, K = map(int, input().split())
a = list(map(int, input().split()))
res = set()
for i in range(N):
    for j in range(i+1, N):
        for m in range(j+1, N):
            res.add(a[i] + a[j] + a[m])
            res = list(res)
            res.sort(reverse=True)
            print(res[k-1])


# 순서도 기록

# N장의 카드, K번째 수 입력받음 --> N개의 값 입력 받음 --> 중복을 제거하기위해 set()선언 ---> 3장을 뽑음 --> 3장의 합을 중복을 제거하기 위해 set()에 넣음
# --> set값을 list로 변환시켜줌(정렬시키기 위해서)  --> k번째 큰값을 찾으므로 내림차순으로 정렬함 ---> k번째 수 출력

# 위의 순서도 대로 다시 기록을 하면
# 1. N, K = map(int, input().split())
# 2. a = list(map(int, input().split()))
# 3. res = set()
# 4. for i in range(n):
#     for j in range(i+1, n):
#      for m in range(j+1, n): 
#     5. res.add(a[i] + a[j] + a[m])
#     6. res = list(res)
#     7. res.sort(reverse = True)

#     8. print([res[k-1]])
