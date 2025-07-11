# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 
# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 
# 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 
# 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

# 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

# 예제 입력 1             예제 출력 1
# 4 5 1                 1 2 4 3
# 1 2                   1 2 3 4
# 1 3
# 1 4
# 2 4
# 3 4

N, M, V = map(int, input().split()) # 정점의 개수 N, 간선의 개수 M, 정점의 번호 V를 받는다.

matrix = [[0] * (N+1) for i in range(N+1)]

for i in range(M):
    a,b = map(int, input().split())
    matrix[a][b] = matrix[b][a] = 1 # 간선이 양방향이므로 값의 위치를 바꿔도 같다.
visit_list = [0]*(N+1)

# dfs 정의
def dfs(V):
    visit_list[V] = 1 # 방문한 점을 1로 표시함
    print(V, end = ' ')
    for i in range(1, N+1):
        if(visit_list[i] == 0 and maxtrix[V][i] == 1):
            dfs(i)

# bfs 정의
def bfs(V):
    queue = [V]
    visit_list[V] = 0
    while queue:
        V = queue.pop(0)
        print(V, end= ' ')
        for i in range(1, N+1):
            if(visit_list[i]==1 and maxtix[V][i]== 1):
                queue.append(i)
                visit_list[i] = 0

dfs(V)
print()
bfs(V)