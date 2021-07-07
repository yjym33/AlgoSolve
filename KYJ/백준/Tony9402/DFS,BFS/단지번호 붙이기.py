# 문제 출처 : https://www.acmicpc.net/problem/2667

dx = [-1, 0, 1, 0]; # 방향
dy = [0, 1, 0, -1];

def DFS(x, y):
    global cnt;
    cnt += 1; # 집 카운팅
    board[x][y] = 0; # 방문 체크
    for i in range(4): # 네방향
        xx = x + dx[i];
        yy = y + dy[i];
        if 0 <= xx < n and 0 <= yy < n and board[xx][yy] == 1:
            DFS(xx, yy);

if __name__ == "__main__":
    n = int(input());
    board = [list(map(int, input())) for _ in range(n)];
    res = []; # 집, 단지
    for i in range(n):
        for j in range(n): # 집 탐색
              if board[i][j] == 1: # 집 발견
                  cnt = 0; # 매 단지마다의 집의 개수
                  DFS(i, j);
                  res.append(cnt); # 단지 집 개수 저장
    print(len(res)); # 단지의 개수
    res.sort(); # 오름차순 정렬
    for x in res: # 단지 출력
        print(x);

# 이중 for문으로 돌며 단지를 검색한다.
  # 1을 발견하면 DFS를 호출하여 집 개수를 카운팅한다.
  # 답을 위한 리스트에 찾은 집 개수 넣기
  # 단지 개수, 집 개수를 출력

# 방문한 집은 0으로 체크
# BFS로 탐색이 가능하다.

# # 다른 사람 풀이

# from sys import stdin
# n = int(input())
# # 데이터 저장용 공간 matrix
# matrix = [[0]*n for _ in range(n)]
# # 방문 내역 저장용 visited
# visited = [[0]*n for _ in range(n)]

# # matrix에 아파트 유무 0과 1 저장
# for i in range(n):
#     line = stdin.readline().strip()
#     for j, b in enumerate(line):
#         matrix[i][j] = int(b)

# # 방향 확인용 좌표 dx와 dy
# # 중앙을 기준으로 좌/우/위/아래
# dx = [-1, 1, 0, 0]
# dy = [0, 0, 1, -1]

# # DFS 함수 정의
# def dfs(x, y, c):
#     visited[x][y] = 1   # 방문 여부 표시
#     global nums            # 아파트 단지 수를 세기위한 변수
#     # 아파트가 있으면 숫자를 세어줍니다.
#     if matrix[x][y] == 1:
#         #matrix[x][y] = c # 아파트 단지별 숫자 표시용
#         nums += 1
#     # 해당 위치에서 좌/우/위/아래 방향의 좌표를 확인해서 dfs 적용
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx < n and 0 <= ny < n:
#             if visited[nx][ny] == 0 and matrix[nx][ny] == 1:
#                 dfs(nx,ny, c)

# cnt = 1 # 아파트 단지 세기 위한
# numlist = [] # 아파트 단지별 숫자
# nums=0 # 아파트 수
# for a in range(n):
#     for b in range(n):
#         if matrix[a][b] == 1 and visited[a][b] == 0:
#             dfs(a,b,cnt)
#             numlist.append(nums)
#             nums = 0
# #            cnt += 1 # 아파트 단지 별 표시용

# print(len(numlist))
# for n in sorted(numlist):
#     print(n)