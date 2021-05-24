https://www.acmicpc.net/problem/9012

T = int(input())

for _ in range(T):
    check = input()
    ls = list(check)
    sum = 0

    for i in ls:
        if i == "(":
            sum += 1
        elif i == ")":
            sum -= 1
        if sum < 0:
            print("NO")
            break

    if sum > 0: # 0보다 크다는 말은 "(" or ")" 가 1개 더 많다는 것이므로 NO 출력
        print("NO")

    if sum == "0": # 0이면 괄호 의 개수가 같으므로 "YES" 출력
        print("YES")    