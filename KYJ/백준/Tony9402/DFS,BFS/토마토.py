# 문제 출처 : https://www.acmicpc.net/problem/7576

import sys
from collections import deque
r = sys.stdin.readline

def bfs(M, N, box):
    dx = [0, 0, 1, -1]
    dy = [-1, 1, 0, 0]

    days = -1

    while ripe:
        days += 1
        for _ in range(len(ripe)):
            x, y = ripe.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if (0 <= nx < N) and (0 <= ny < M) and (box[nx][ny] == 0):
                    box[nx][ny] = box[x][y] + 1
                    ripe.append([nx, ny])

    for b in box:
        if 0 in b:
            return -1
    return days


M, N = map(int, r().split())
box, ripe = [], deque()
for i in range(N):
    row = list(map(int, r().split()))
    for j in range(M):
        if row[j] == 1:
            ripe.append([i, j])
    box.append(row)


print(bfs(M, N, box))

# BFS를 사용해서 밭에 있는 토마토가 모두 익으려면 얼마나 걸리는지 구하는 문제이다.
# 하루가 지날 때마다 익은 토마토 상하좌우 토마토들이 익게 된다.