# 문제 링크 : https://www.acmicpc.net/problem/1874

n = int(input())
stack = []
result =[]
count = 0
x = True


for _ in range(n):
    num = int(input())

while count < num:
    count += 1
    stack.append(count)
    result.append("+")

if stack[-1] == num:
    stack.pop()
    result.append("-")
else:
    x = False
    break

if x == False:
    print('NO')
else:
    for i in result:
        print(i)


# key point 1
# stack이 저장할 리스트와 result로 포현할 리스트를 따로 설정, count 변수 0으로 초기화, possible 변수 설정하여 불가능 할 경우 "NO" 출력

# key point 2
# while 반복문을 통해 count가 입력받은 num보다 작을때 돌아가게끔 해주고, stack이 비어있을 경우를 대비해 1을 증가시켜준다.
# 그리고 stack 의 append 함수를 이용해 count의 수인 1을 push 해준다.
# 그리고 result에는 stack에 push가 된 것이므로 "+"를 append 해주면 된다.

# key point 3
# 다음으로 top 가장 꼭대기에 있는 것을 stack[-1]로 지정해준다.
# if 문을 통해서 만약 top이 num으로 들어온 수와 같다면
# pop을 통해 그 수를 빼주고 result 에는 '-' 를 추가해준다.

# 반대로 else 에서 top이 num으로 들어온 숫자와 같지 않다면, possible 를 False로 초기화시켜주고 break 해준다.

# 이제 마지막으로 possible가 False이면 "NO" 를 출력하고 아닐 경우에는 result에 저장된 문자열들을 for문을 통해 돌면서 출력해준다.