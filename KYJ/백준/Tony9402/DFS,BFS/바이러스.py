# queue 사용을 위해 deque 선언
from collection import deque

n = int(input()) # 컴퓨터의 수
p = int(input()) # 연결된 쌍의 수

computer=[]
for i in range(n+1):
    computer.append([])

for i in range(pair):
    a,b = map(int, input().split())
    computer[a].append(b)

# 바이러스의 감염 여부를 확인할 리스트 만들기
virus = [0] * (n+1)
virus[1] = 1

# bfs 함수 만들기
def bfs(computer):
    queue = deque()
    queue.append(1)
    count = 0
    # 큐가 진행되는 동안
    while queue:
        v = queue.popleft()
        # 현재 주어진 컴퓨터에 연결된 컴퓨터 찾기
        for com in computer[v]:
            if virus[com] == 0:
                virus[com] = 1
                queue.append(com)
                count += 1
    return count

print(bfs(computer))