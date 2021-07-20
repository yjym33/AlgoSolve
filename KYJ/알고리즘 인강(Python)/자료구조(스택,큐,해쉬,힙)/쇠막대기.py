s = input()
stack = []
cnt = 0
for i in range(len(s)):
    if s[i] == '(':
        stack.append(s[i]) # 여는 괄호면 무조건 stack에 쌓는다.
    else:
        stack.pop()
        if s[i-1] == '(':
            cnt += len(stack) # 레이저 이므로 stack에서 빼주고 cnt 에 스택의 길이만큼 더해준다.
        else:
            cnt += 1
print(cnt)


