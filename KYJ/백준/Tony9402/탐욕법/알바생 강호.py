# https://www.acmicpc.net/problem/1758

# 풀이 1

n = int(input()) #사람의 수 N이 주어짐
tip = [] #tip을 넣을 리스트 생성
for _ in range(n):
    a = int(input())
    tip.append(a) 
tip.sort(reverse = True) #줄 (선사람의 생각하는 팁을 받아와 큰 순서대로 배열

rate = 1 #등수 초기화
result = 0 #결과값 초기화
for i in tip:
    if (i - (rate-1)) >= 0: #(주려고생각한 팁 - (받은등수 - 1)) 이 음수가 아닌 경우만 알고리즘 생성
        result = result + (i - (rate-1))
        rate += 1
    else:
        continue
print(result)

# 이 문제의 핵심은 팁을 받은 순서를 큰 순서대로 리스트에 배열하는 것이다.
# 만약 1 1 9 9 가 주어진다고 한다면, 작은숫자 즉 1이 줄의 뒤로 가게 된다면
# 돈 - (받은 등수 - 1)의 값이 음수가 나오게 된다. 따라서 1은 2번쨰 부터 0의 값이 나오게 되므로 어디서 줄을서도 어차피 팁은 0원 이다.
# 하지만 큰 숫자들은 뒤로 갈수록 원래 주려고 했던 팁이 줄어든다. 즉 팁을 최대로 받을 수 있는 최적의 방법에서 멀어진다는 애기이다.


# # 풀이 2

# import sys
# input = sys.stdin.readline()
# n = int(input())
# arr = [int(input() for _ in range(n))]

# arr.sort(reverse = True)
# sum = 0

# for i in range(n):
#     if arr[i] - i < 0:
#         continue
#     sum += (arr[i] - i)

# print(sum)

# #  강호가 최대의 팁을 얻어야 하므로 입력받는 고객의 팁을 역순으로 정렬해서 풀면 된다. 
# # 또한 이후 강호가 받게 되는 팁이 음수가 된다면 아무것도 받지 않는 부분만 코드에 추가해 주면 된다.

 