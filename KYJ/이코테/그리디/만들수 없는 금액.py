# N개의 동전을 가지고 있을 때, N개의 동전을 이용하여 만들 수 없는 양의 정수 금액중 최솟값을 구하는 프로그램을 작성하시오.

# ex) N = 5이고, 각각 3원, 2원, 1원, 1원, 9원이 주어질때 만들 수 없는 양의 정수 금액중 최소값은 8입니다.

n = int(input()) # 동전의 개수 
data = list(map(int, input().split())) # 화폐의 단위를 받아옴
data.sort()

target = 1
for x in data:
    # 만들수 없는 금액을 찾으면 종료
    if target < x:
        break
    else:
        target += x

print(target)

# 디버깅 

# n = 5 / data = [3, 2, 1, 1, 9] / data.sort = [1, 1, 2, 3, 9] / target = 1

# if target < x  / else: target += x

#  1 < 1  -> target += 1 => target = 2
#  2 < 1  -> target += 1 => target = 3
#  3 < 2  -> target += 2 => target = 5
#  5 < 3  -> target += 3 => target = 8
#  8 < 9  -> target < x  이므로 break 종료
#  따라서 만족하는 target중 가장 큰수는 8이다.