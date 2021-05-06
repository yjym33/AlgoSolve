from collections import deque
# 리스트로도 큐(Queue)를 구현할수 있으나 시간복잡도에 있어서 효율이 좋지 못하기 떄문에 deque를 사용하는 것이 좋다.

# 큐(Queue) 구현을 위해 deque 라이브러리 사용
queue = deque()

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft() # 가장 왼쪽에 있는 데이터를 꺼낼때 사용
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)   # 먼저 들어온 순서대로 출력
queue.reverse() # 다음 출력을 위해 역순으로 바꾸기
print(queue)    # 나중에 들어온 원소부터 출력

# 먼저 들어온 데이터가 먼저 나가는 형식(선입선출)의 자료구조
# 큐는 입구와 출구가 모두 뚫려 있는 터널과 같은 형태로 시각화 할수 있습니다.

# queue에서 삽입은 append(), 삭제는 popleft()를 사용합니다.