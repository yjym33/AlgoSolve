# 문제 출처 : https://www.acmicpc.net/problem/16954

from sys import stdin
from collections import deque


def visitable(x, y, visited):
    return 0 <= x < 8 and 0 <= y < 8 \
           and graph[x][y] == '.' and not visited[x][y]


def bfs(start):
    q = deque([start])
    dirs = ((0, 0),
            # 상하좌우
            (0, 1), (0, -1), (1, 0), (-1, 0),
            # 대각선
            (1, 1), (1, -1), (-1, 1), (-1, -1))

    while q:
        # 벽이 이동한 후에, 다시 체크해줘야한다.
        visited = [[False] * 8 for _ in range(8)]
        for _ in range(len(q)):
            cur_x, cur_y = q.popleft()

            if [cur_x, cur_y] == [0, 7]:
                return 1

            if graph[cur_x][cur_y] == '#':
                continue

            for x, y in dirs:
                next_x, next_y = cur_x + x, cur_y + y

                if visitable(next_x, next_y, visited):
                    visited[next_x][next_y] = True
                    q.append([next_x, next_y])

        # 행을 아래로 이동
        graph.pop()
        graph.insert(0, ['.', '.', '.', '.', '.', '.', '.', '.'])

    return 0


if __name__ == '__main__':
    graph = [list(stdin.readline().strip()) for _ in range(8)]
    print(bfs([7, 0]))


# 8x8의 체스판이 있을 때, 총 9가지의 경우의 수에 따라 움직일 수 있다. 
# 경우의 수는 상, 하, 좌, 우, 대각선 그리고 현재 위치에 그대로 있는 경우이다. 
# 또한 다른 문제와 다른 점이 있다면 체스판이 아래로 이동하여 그래프의 상태가 변화한다는 것이다.

# current	  |	  after 1 sec
# ........	  |	    ........
# ........	  |	    ........
# ........	  |	    ........
# ........	  |	    ........
# ........	  |	    ........
# ........	  |	    ........
# ##......	  |	    ........
# ........	  |	    ##......

# 따라서 현재 이동할 수 있는 경우의 수는 현재 위치, 현재 위치의 우측 칸이다. 
# 하지만 1초 후에는 현재 위치들이 벽이 되므로 더 이상 이동할 수 없어, 오른쪽 끝으로 이동할 수 없다.
# 문제를 풀기 위해서는 BFS를 이용한 그래프 탐색과 동일하게 풀되 현재 방문한 지점이 벽이라면 더 이상 경우에 수에 추가하지 않도록 해야 한다. 
# 또한 중요한 것은  visited를 그래프가 이동한다면 초기화하고 다시 체크해줘야 한다는 것이다.
# 즉, 시간에 따라 그래프가 변화하면 다른 그래프이고, 다른 경우의 수를 반영하여야 하므로 visited를 다른 문제들과 같이 계속 유지하는 것이 아닌 초기화해주어야 하는 것이다.