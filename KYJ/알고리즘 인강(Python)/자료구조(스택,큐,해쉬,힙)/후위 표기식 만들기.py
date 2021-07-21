a = input()
stack = []
res =''
for x in a:
    if x.isdecimal(): # 숫자면 그대로 출력
        res += x
    else:
        if x =='(': # '(' 여는 괄호인 경우 stack에 그대로 넣어준다.
            stack.append(x)
        elif x == '*' or '/': # x가 "*" or "/" 일 경우
            while stack and (stack[-1] == '*' or stack[-1] == '/'): # 스택의 상단에 있는 연산자가 '*' or '/'일 때까지 반복문을 돈후
                res += stack.pop() # 스택에서 꺼낸다.
            stack.append(x)
        elif x == '+' or x == '-':
            while stack and stack[-1]!= '(':
                res += stack.pop()
            stack.append(x)
        elif x == ')':
            while stack and stack[-1]!= '(':
                res += stack.pop()
            stack.pop()
while stack:
    res += stack.pop()
print(res)

