# 스택 문제

num, m = map(int, input().split()) # 숫자 두개를 받는다.
num = list(map(int, str(num))) # num을 리스트화 시킨후 문자열로 변환하여 각 숫자를 자름
stack=[]
for x in num:
    while stack and m>0 and stack[-1]<x:
        stack.pop()
        m -= 1
    stack.append(x)
if m!=0:
    stack = stack[:-m]
# for x in stack:
#     print(x, end = '')
res = ''.join(map(str, stack))
print(res)
