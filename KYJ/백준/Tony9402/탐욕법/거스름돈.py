# https://www.acmicpc.net/problem/14916

n = int(input())
if n in [1,3]: # 5 이상의 수부터는 전부 2와 5로 나누어 떨어지기 떄문에 [1,3]만 포함되지 않으면 된다.
    result -1
elif (n%5)%2 == 0: 
    result = (n//5) + (n%5)//2
else:
    result = ((n//5)-1) + ((n%5+5)//2) # 13같은 경우 5로 나누었을때 3이 남는데 이같은 경우는 5에서 1을 빼주고 이만큼 2에 더해주어야 한다.
print(result)