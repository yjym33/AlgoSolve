# 문제 출처 : https://www.acmicpc.net/problem/16234

from collections import deque

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

def bfs(x, y):
    visited = set([(x, y)])
    q = deque([(x, y)])

    """
    total : 연합의 인구수
    num : 연합에서 나라의 갯수
    """
    total, num = 0, 0

    while q:
        x, y = q.popleft()

        # 방문한 현재 나라의 인구수를 연합의 인구수에 더해주고, 연합에 속한 나라도 증가해준다.
        total += board[x][y]
        num += 1

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if nx >= 0 and nx < n and ny >= 0 and ny < n and (nx, ny) not in visited\
                and (nx, ny) not in total_visited:

                diff = abs(board[nx][ny] - board[x][y])
                if diff >= l and diff <= r:
                    # BFS를 한 번이라도 탄 것이므로, is_move를 True로 변환.
                    global is_move
                    is_move = True

                    q.append((nx, ny))
                    visited.add((nx, ny))

    # 이 연합의 바뀔 인구수와, 연합에 속한 나라(좌표)들을 반환한다.
    return total // num, visited

n, l, r = list(map(int, input().split()))
board = [list(map(int, input().split())) for _ in range(n)]
answer = 0

while True:
    total_visited = set() # BFS 탐색에 한번이라도 들어간 경우, 재 탐색을 할 필요가 없으므로,
                          # 이 집합에 담아둔다.
    is_move = False       # 한 번이라도 BFS를 타게되면 True로 바뀐다.
    unions = []           # (바뀔 인구수, 연합의 좌표들)을 담는다.

    # 먼저, 연합들을 찾아서 unions에 담는다.
    for i in range(n):
        for j in range(n):
            if (i, j) not in total_visited:
                changed_num, visited = bfs(i, j)
                unions.append((changed_num, visited))
                total_visited |= visited

    # 찾은 연합들의 좌표들을 일괄적으로 바꿔준다.
    for (changed_num, union) in unions:
        for country in union:
            x, y = country
            board[x][y] = changed_num

    # 한 번이라도 BFS를 타고들어갔는지 확인한다.
    if not is_move:
        break
    answer += 1

print(answer)


# 1. 초기 접근
# 삼성 기출문제로 대표적인 DFS, BFS 문제이다.
# 인접한 칸으로 탐색해야 하고, 특정 조건 (인접한 칸의 값이 L 이상 R 이하) 인 경우, 더 파고들어 계속 탐색해야 한다.
# BFS를 사용하여 풀어보아야 한다.

# 2. 알고리즘
# 먼저, 현재 상태에서 문제에서 말하는 연합(union) 인 좌표들을 먼저 다 찾아내야 한다.
# 이 과정에서 BFS를 쓴다. 연합인 좌표들은 자연스레 visited 에 들어가게 된다.
# BFS로 탐색하며, 연합인 좌표들의 값을 모두 더하고(total), 그 갯수(num)를 확인해야 한다.
# 이렇게 찾아낸 연합 하나에 들어가는 좌표들(visited) 과 바뀔 값 (total // num) 을 특정 리스트 (unions)에 저장해놓자.
# 현재 상태에서 위 처럼 연합을 다 찾고나면, unions 라는 리스트에 이제 처리해야할 연합들이 있다.
# 이게 핵심인데, BFS로는 연합을 찾기만 하고, BFS가 끝난 후, 값 변환은 한 번에 해야한다.
# 왜냐하면 BFS하는 와중에 값을 바꿔버리면, 현재 인구상태가 수정되게 되고, 이후 BFS에 영향을 주기 때문이다.
# 한 번이라도 BFS를 타고 들어가는지 체크하여(is_move), 한 번도 들어가지 않는다면 종료한다.
