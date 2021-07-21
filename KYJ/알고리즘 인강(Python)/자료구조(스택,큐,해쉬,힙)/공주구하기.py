from collections import deque
n, k = map(int, input().split())

dq = list(range(1, n+1))
dq = deque(dq) # dq를 deque 자료구조로 만듬
while dq:
    for _ in range(k-1):
        cur = dq.popleft()
        dq.append(cur)
    dq.popleft() # 7~10까지 하나의 패턴(규칙)
    if len(dq) == 1:
        print(dq[0]) # 하나만 남았을때 출력
        dq.popleft()
