# 문제 링크 : https://www.acmicpc.net/problem/1541

s = input().split('-')

sum = 0

for i in s[0].split('+'):
    sum += int(i) 
# sum = 55

for i in s[1:]: 
    for j in i.split('+'):
        sum -= int(j)


print(sum)

# 최솟값을 만들기 위해서 -가 존재할 시, 다음 -가 오기 전까지 모든 수를 괄호로 묶어 더해주면 된다. 
# 즉 처음 -(마이너스)가 나온뒤로는 다 빼주면 된다. (처음 -나온 후부터 뒤에 값들은 -취급한다.)

# 다른 풀이

# expression = input().split("-")

# for i in range(len(expression)):
#     expression[i] = expression[i].split("+")

# total_sum = 0
# for i in range(len(expression[0])):
#     total_sum += int(expression[0][i])

# for i in range(1, len(expression)):
#     num_sum = 0
#     for j in range(len(expression[i])):
#         num_sum += int(expression[i][j])

#     total_sum -= num_sum

# print(total_sum)


# 최고의 풀이

# n = [sum(int(x) for x in y.split('+')) for y in input().split('-')]
# print(n[0] - sum(n[1:]))