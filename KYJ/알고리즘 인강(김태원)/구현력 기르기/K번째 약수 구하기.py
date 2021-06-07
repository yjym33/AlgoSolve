# K번째 약수

# 어떤 자연수 p와 q가 있을 때, 만일 p를 q로 나누었을 때 나머지가 0이면 q는 p의 약수이다.
# 두개의 자연수 n과 k가 주어졌을때 n의 약수들중 k번째로 작은수를 출력하는 프로그램을 작성하시오.

n, k = map(int,input().split())
cnt = 0

for i in range(1, n):
    if n % i == 0:
        cnt += 1
    if cnt == k:
        print(i)
        break
else:
    print (-1)