# 문제 출처 : https://www.acmicpc.net/problem/1931

N = int(input())
time = []

for _ in range(N):
  start, end = map(int, input().split())
  time.append([start, end])

time = sorted(time, key=lambda a: a[0]) # 시작 시간을 기준으로 오름차순
time = sorted(time, key=lambda a: a[1]) # 끝나는 시간을 기준으로 다시 오름차순

last = 0 # 회의의 마지막 시간을 저장할 변수
conut = 0 # 회의 개수를 저장할 변수

for i, j in time:
  if i >= last: # 시작시간이 회의의 마지막 시간보다 크거나 같을경우
    conut += 1
    last = j

print(conut)

# 주어진 시작시간과 끝나는 시간들을 이용해서 가장 많은 회의의 수를 알기 위해서는 빨리 끝나는 회의 순서대로 정렬을 해야 한다. 
# 이유는 빨리 끝날수록 뒤에서 고려해볼 회의가 많기 때문이다. 
# 빨리 시작하는 순서대로 정렬을 우선시 한다면, 오히려 늦게 끝날 수 있기 때문이다.

# 그래서 먼저 시작시간을 오름차순으로 정렬한 뒤, 끝나는 시간을 기준으로 한번 더 정렬을 해야 한다.
# 이미 시작시간이 오름차순으로 정렬된 상태이기 때문에 끝나는 시간으로 오름차순을 해주어도 자연히 끝나는 시간이 같을 때에는 시작시간의 오름차순으로 정렬이 되어있다.

# 정렬된 이후에 시작시간과 끝나는시간을 비교한다.
# 마지막 회의 시간을 저장할 변수 last와 회의의 수 count를 선언한후, 
# 시작시간과 last를 비교하여 시작시간이 last보다 크거나 같으면 count를 1 증가시키고 last변수에 회의 마지막 시간을 대입한다.

