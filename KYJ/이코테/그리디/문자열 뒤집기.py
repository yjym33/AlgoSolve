data = input()

count0 = 0
count1 = 0

if data[0] == "1":
    count0 += 1
else:
    count1 += 1

for i in range(len(data)-1):
    if data[i] != data[i+1]:
        if data[i+1] == "1":
            count0 += 1
        else:
            count1 += 1

print (min(count0, count1))

# 0으로 만들때와 1로 만들때 경우의 수를 각각 세어서 더 작은수를 출력하는 문제

# 앞에서부터 하나씩 확인하면서 0 에서 1로 바꾸거나 1에서 0으로 바꾸거나 하는 방식으로 문제를 해결해야 한다.
