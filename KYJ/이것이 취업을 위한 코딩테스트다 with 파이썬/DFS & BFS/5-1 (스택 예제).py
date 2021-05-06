stack = []

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack[::-1])   # 최상단 원소부터 출력
print(stack)    # 최하단 원소부터 출력

# Stack은 먼저 들어오는 데이터가 나중에 나가는 (선입후출)의 자료구조입니다.
# 입구와 출구가 동일한 형태로 스택을 시각화 할수 있습니다. (ex : 박스쌓기)


# stack에서 삽입은 append(), 삭제는 pop()를 사용합니다.