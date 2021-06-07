# N개의 자연수가 입력되면 각 자연수의 자릿수의 합을 구하고, 그 합이 최대인 자연수를 출력하는 프로그램을 작성하세요.
# 각 자연수의 자릿수의 합을 구하는 함수를 def digit_sum(x)를 꼭 작성해서 프로그래밍 하세요.

# 입력설명

# 첫 줄에 자연수의 개수 N(3<= N <= 100)이 주어지고, 그 다음에 N개의 자연수가 주어진다.
# 각 자연수의 크기는 10.000.000을 넘지 않는다.

# 출력설명

# 자릿수의 합이 최대인 자연수를 출력한다.

# 입력예제 1

# 3

# 125 15232 97

# N = int(input())
# a = list(map(int, input().split()))

# def digit_sum(x):
#     sum = 0

#     while > 0:
#         sum = 0
#         sum += x % 10
#         x = x // 10
#     return sum

N = int(input())
a = list(map(int, input().split()))

def digit_sum(x):
    sum = 0
    for i in str(x):
        sum += int(i)
    return sum

max = -2147000000

for x in a:
    tot = digit_sum(x)
    if tot > max:
        tot = max
        res = x
print(res)
        







