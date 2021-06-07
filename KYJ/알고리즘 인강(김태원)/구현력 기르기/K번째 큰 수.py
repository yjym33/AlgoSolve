# K번째 큰 수

# 현수는 1부터 100사이의 자연수가 적힌 N장의 카드를 가지고 있습니다. 같은 숫자의 카드가 여러장 있을수 있습니다.
# 현수는 이 중 3장을 뽑아 각 카드에 적힌 수를 합한 값을 기록하려고 합니다.
# 기록한 값 중 K번째로 큰 수를 출력하는 프로그램을 작성하세요.
# 만약 큰 수부터 만들어진 수가 25 25 23 23 22 20 19 .... 이고 K값이 3이라면 K번째 큰 값은 22 입니다.

# 입력 설명

# 첫 줄에 자연수 N (2 <= N <= 100)과 K(1 <= K <= 50) 입력되고, 그 다음 줄에 N개의 카드값이 입력된다.

# 출력 설명

# 첫 줄에 K번째 수를 출력합니다.

# 입력 예제 1

# 10 3
# 12 15 24 22 45 65 33 11 26 42

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
