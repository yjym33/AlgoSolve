n, m = map(int, input().split())

ball_weight = list(map(int,input().split()))

weight_list = [0] * (m+1)

for weight in ball_weight:
    weight_list[weight] += 1

cnt = 0

for i in range(1, m+1):
    n = weight_list[i]
    cnt += weight_list[i] * n

print(cnt)

# 전체 개수에서 첫번째 고른 사람이 고른 볼링공의 갯수 제외
# 고르는 개수 카운트