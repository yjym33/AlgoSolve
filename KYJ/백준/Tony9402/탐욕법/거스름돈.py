# https://www.acmicpc.net/problem/14916

n = int(input())
if n in [1,3]: # 5 이상의 수부터는 전부 2와 5로 나누어 떨어지기 떄문에 [1,3]만 포함되지 않으면 된다.
    result -1
elif (n%5)%2 == 0: 
    result = (n//5) + (n%5)//2
else:
    result = ((n//5)-1) + ((n%5+5)//2) # 8 or 13 같은 경우 5로 나누었을때 나머지가 3이다. 3은 2로 나누어떨어지지 않으므로 5를 하나 빼주고 그만큼 2에 더해준다.
print(result)