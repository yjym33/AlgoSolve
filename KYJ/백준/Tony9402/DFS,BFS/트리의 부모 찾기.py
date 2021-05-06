# 루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.

# 첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.
# 첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.


from collections import deque

n=int(input())
graph={i:[] for i in range(1,n+1)}
parents=[0]*n

for i in range(n-1):
  x,y=map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)

queue=deque()
queue.append(1)

while queue:
  temp=queue.popleft()
  for i in graph[temp]:
    if parents[temp-1]!=i:
      parents[i-1]=temp
      queue.append(i)

for i in parents[1:]:
  print(i)