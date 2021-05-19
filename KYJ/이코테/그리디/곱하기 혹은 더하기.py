data = input() # 문자열 받아오기

# 첫번째 문자를 숫자로 변경해서 대입
answer = int(data[0])

for i in range(1, len(data)):
    # 두 수중에 하나라도 '0'또는 '1' 일 경우 곱하기 연산보다는 더하기 연산 수행
    if int(data[i]) < 2 or answer < 2:
        answer += int(data[i])
    else:
        answer *= int(data[i])

print(answer)


# 문제의 조건이 무조건 왼쪽에서부터 시작한다고 했으므로 그리디 알고리즘으로 풀어야 한다.
# 문제의 핵심은 2 미만, 0 or 1이 나오면 더하기 연산, 2부터는 곱하는것이 더 커지므로 곱하기 연산을 해야한다.
