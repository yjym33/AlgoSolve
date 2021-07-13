# 문제 출처 : https://www.acmicpc.net/problem/13549

import sys
from collections import deque

n, k = map(int, input().split())

q = deque()
vis = [-1] * 200001
q.append(n)
vis[n] = 0

while q:
    x = q.popleft()
    if x == k:
        print(vis[x])
        sys.exit()
    # 순간이동해서 갈수 있는곳을 구한다.
    if x * 2 <= 200000 and vis[x * 2] == -1:
        vis[x * 2] = vis[x]
        # appendleft를 통해 큐의 앞에 넣어 해당 초에 방문할 수 있도록 한다.
        q.appendleft(x * 2)
    # x-1 로 갈수 있는곳 1초 더한다.
    if x - 1 >= 0 and vis[x - 1] == -1:
        vis[x - 1] = vis[x] + 1
        q.append(x - 1)
    # x+1 로 갈 수 있는곳 1초 더한다.
    if x + 1 <= 200000 and vis[x + 1] == -1:
        vis[x + 1] = vis[x] + 1
        q.append(x + 1)

# 수빈이는 다음의 3가지 행동을 취할수 있습니다.
# 1. 1초후에 x-1로 이동한다. (걷는경우)
# 2. 1초후에 x+1로 이동한다. (걷는경우)
# 3. 0초후에 x*2로 이동한다. (순간이동)

# 일단 이 문제는 목적지까지의 최단거리를 구하는 문제이므로 (걷는 것과 순간이동하는 것중 최단거리를 구해야 하므로)
# 이 문제는 bfs를 활용하여 문제를 풀수 있습니다.
# 
# 이 문제의 핵심은  0초 후에 X*2로 이동하는 것을 어떻게 구현하는가? 입니다.
# 그 방법은 수빈이가 k초 있는 지점에서 200,000 전까지의 k*2 (순간이동)을 전부 방문처리한 후,
# 큐의 맨 앞에 넣는 것입니다. 그렇게 한다면 k초에 해당하는 지점을 전부 방문할수 있습니다.


