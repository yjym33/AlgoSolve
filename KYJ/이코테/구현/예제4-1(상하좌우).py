# 여행가 A는 N x N 크기의 정사각형 공간 위에 서 있습니다.
# 이 공간은 1 x 1 크기의 정사각형으로 나누어져 있습니다.
# 가장 왼쪽 위 좌표는 (1.1)이며, 가장 오른쪽 아래 좌표는(N,N)에 해당합니다.
# 여행가 A는 상, 하, 좌, 우 방향으로 이동할 수 있으며, 시작 좌표는 항상 (1,1)입니다.
# 우리 앞에는 여행가 A가 이동할 계획이 적힌 계획서가 놓여 있습니다.
# 계획서에는 하나의 줄에 띄어쓰기를 기준으로 하여, L,R,U,D 중 하나의 문자가 반복적으로 적혀 있습니다.
# 각 문자의 의미는 다음과 같습니다.

#     * L : 왼쪽으로 한 칸 이동
#     * R : 오른쪽으로 한 칸 이동
#     * U : 위로 한 칸 이동
#     * D : 아래로 한 칸 이동

# 이때 여행가 A가 N x N 크기의 정사각형 공간을 벗어나는 움직임은 무시됩니다.
# 예를 들어 (1,1)의 위치에서 L 혹은 U를 만나면 무시됩니다. 다음은 N = 5인 지도와 계획서입니다.

#         계획서와 지도
#   R -> R -> R -> U -> D -> D
# (1,1) (1,2) (1,3) (1,4) (1,5)
# (2,1) (2,2) (2,3) (2,4) (2,5)
# (3,1) (3,2) (3,3) (3,4) (3,5)
# (4,1) (4,2) (4,3) (4,4) (4,5)
# (5,1) (5,2) (5,3) (5,4) (5,5)

# 이 경우 6개의 명령에 따라 여행가가 움직이게 되는 위치는 순서대로
# (1,2), (1,3), (1,4), (1,4), (2,4), (3,4)이므로,
# 최종적으로 여행가 A가 도착하게 되는 곳의 좌표는 (3,4)이다.
# 다시말해 3행 4열의 위치에 해당하므로 (3,4)라고 적는다.
# 계획서가 주어졌을 때 여행가 A가 최종적으로 도착할 지점의 좌표를 출력하는 프로그램을 작성하시오.

# 입력 조건 : 첫째 줄에 공간의 크기를 나타내는 N이 주어진다. (1 =<N =<100)
#          둘째 줄에 여행가 A가 이동할 계획서 내용이 주어진다. (1 =< 이동 횟수 =< 100)

# 출력 조건 : 첫째 줄에 여행가 A가 최종적으로 도착할 지점의 좌표 (X,Y)를 공백으로 구분하여 출력한다.

# 입력 예시 : 5, R R R U D D                           출력 예시 : 3 4
# ---------------------------------------------------------------------------------------------------------------------------
# 풀이 (Python)

N = int(input())
command = input().split()
x, y = 1, 1
for i in command:
    if i == "L" and y > 1 : y -= 1
    elif i == "R" and y < N : y += 1
    elif i == "U" and x > 1 : x -= 1
    elif i == "D" and x < N : x += 1

print(x, y)

# 행렬좌표 x, y는 이차원배열과 반대인 것에 주의해야함

# ---------------------------------------------------------------------------------------------------------------------------
# 풀이 (Python)

# N을 입력받기
n = int(input())
x, y = 1, 1  # 현재 위치를 의미 (시작지점 1,1)
plans = input().split()  # 이동경로

# L, R, U, D에 따른 이동 방향 (방향벡터)
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny

print(x, y)
# ---------------------------------------------------------------------------------------------------------------------------
# 이 문제는 요구사항대로 충실히 구현하면 되는 문제입니다.
# 이러한 문제는 일련의 명령에 따라서 개체를 차례대로 이동시킨다는 점에서 시뮬레이션 유형으로 분류되며 구현이 중요한 대표적 문제 유형입니다.
#  - 다만, 알고리즘 교재나 문제 풀이 사이트에 따라서 다르게 일컬을 수 있으므로,
#    코딩테스트에서의 시뮬레이션 유형, 구현 유형, 완전 탐색 유형은 서로 유사한 점이 많다는 정도로만 기억합시다.
