# 행(Row)이 3개인 2차원 리스트로 인접 리스트 표현
graph = [[] for _ in range(3)]

# 노드 0에 연결된 노드 정보 저장(노드, 거리)
graph[0].append((1,7))
graph[0].append((2,5))

# 노드 1에 연결된 노드 정보 저장 (노드, 거리)
graph[1].append((0,7))

# 노드 2에 연결된 노드 정보 저장 (노드, 거리)
graph[2].append((0, 5))

print(graph)

# 인접 행렬과 인접 리스트는 어떤 차이가 있을까?

# 메모리 측면에서 보자면 인접 행렬 방식은 모든 관계를 저장하므로 노드 개수가 많을수록 메모리가 불필요하게 낭비된다,
# 반면에 인접 리스트 방식은 연결된 정보만을 저장하기 떄문에 메모리를 효율적으로 사용한다.
# 하지만 이와 같은 속성 때문에 인접 리스트 방식은 인접 행렬 방식에 비해 특정한 두 노드가 연결되어 있는지에 대한 정보를 얻는 속도가 느리다.
# 인접 리스트 방식에서는 연결된 데이터를 하나씩 확인해야 되기 때문이다.
# 그러므로 특정한 노드와 연결된 모든 인접 노드를 순회하는 경우, 인접 리스트 방식이 인접 행렬 방식에 비해 메모리 공간의 낭비가 적다.
