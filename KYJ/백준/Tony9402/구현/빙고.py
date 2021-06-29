# 문제 출처 : https://www.acmicpc.net/problem/2578

bingo = []
for _ in range(5):
    bingo.append(list(map(int, input().split())))

num = list(map(int, input().split()))
for _ in range(4):
    num += list(map(int, input().split()))

check = [0] * 12 #바뀐것의 갯수 저장하는 리스트 idx0~4는 row / 5~9는 col / 10, 11은 대각
line = 0
flag = False
for n in range(25): #사회자가 하나씩 부른다.
    if flag == True:
        break
    for i in range(5): #빙고탐색
        if flag == True:
            break
        for j in range(5):
            if flag == True:
                break
            if num[n] == bingo[i][j]: #사회자가 부른거 찾으면
                bingo[i][j] = 0 #0 으로 바꾸고
                check[i] += 1 #행 바뀐거 체크
                check[j+5] += 1 #열 바뀐거 체크
                if i == j: #대각
                    check[10] += 1
                if i + j == 4: #반대대각
                    check[11] += 1
                for c in range(12): #바뀐것 갯수 저장하는 리스트 탐색해서
                    if check[c] == 5: #5번 바뀌었으면
                        check[c] = 0 # 초기화시키고
                        line += 1 #빙고처리
                        if line == 3:
                            flag = True
                            break
print(n)


# 또다른 코드

def isBingo(arr):
    cnt = 0
    # 가로 빙고 여부 확인
    for l in arr:
        if l.count(0) == 5: 
            cnt += 1
    # 세로 확인
    for i in range(5): 
        y = 0
        for j in range(5):
            if arr[j][i] == 0:
                y += 1
        if y == 5:
            cnt += 1
    # 대각선(\) 확인
    k = 0
    for i in range(5): 
        if arr[i][i] == 0:
            k += 1
    if k == 5:
        cnt += 1
    # 대각선(/) 확인
    u = 0
    for i in range(5): 
        if arr[i][4-i] == 0:
            u += 1
    if u == 5:
        cnt += 1
    return cnt

bingo = [] # 빙고판
tutor = [] # 하나씩 부를 숫자
for _ in range(5):
    b = list(map(int, input().split()))
    bingo.append(b)
for i in range(5):
    w = list(map(int, input().split()))
    for j in w:
        tutor.append(j)
for idx, num in enumerate(tutor):
    for m in bingo: # 첫 번째 줄부터 차례로 체크
        if num in m: # 부르는 숫자가 해당 줄에 있으면
            m[m.index(num)] = 0 # 숫자를 0으로 변환
            break
    res = isBingo(bingo) # 맞은 줄이 몇 개인지 확인
    if res >= 3:
        print(idx+1)
        break


# 빙고가 완성되는것을 어떻게 파악하는가가 중요하다.
# 이 문제는 완벽한 구현 문제로
# 가로, 세로, 대각선(우), 대각선(좌)를 어떤식으로 구현할지, 어떤식으로 체크를 해야할지를 단순무식하게 푸는 방법밖에 없다.
