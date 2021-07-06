#  문제 출처 : https://www.acmicpc.net/problem/10870

# 재귀함수 코드
def fibonacci(n):
    if n<=1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)

n=int(input())
print(fibonacci(n))

# for문 코드

n = int(input())

fibonacci = [0, 1]
for i in range(2, n+1):
    num = fibonacci[i-1] + fibonacci[i-2]
    fibonacci.append(num)
print(fibonacci[n])

# 이번 문제는 임의의 수가 주어지면 피보나치 값을 출력하는 문제이다. 

# 1-1 피보나치수열 (재귀)
# 처음 두수를 0과 1로 하고, 그 다음부터는 자기 앞의 두수를 더한수의 나열이다.

# if 조건식을 이용해서 입력받는 수 n이 1보다 작은 경우, 즉 0과 1인 경우는 그대로 n을 return 하고 
# 0과 1이 아닌 경우에는 앞의 두 수를 더한 값을 return 하도록 하였다. 
# 이때, 앞의 두 수를 불러낼 때 함수 자기 자신을 불러오는 재귀 함수를 이용해서 코드를 작성하였다. 

# for문 (반복문)을 이용한 피보나치수열

# 우선 fibonacci라는 숫자 리스트로 이루어진 변수를 선언한다. 
# 먼저 리스트에는 0과 1을 요소로 지정한다. 
# range함수를 이용해서 2부터 입력받는 수 n까지의 숫자 범위를 생성한다. 
# 이 숫자는 fibonacci 리스트의 인덱스로 사용된다. 

# 이후 for문에서 range 함수로 생성된 숫자 변수 i를 이용해서 fibonacci 리스트의 마지막 두 수의 위치를 구한다. 
# fibonacci [i-1]과 fibonacci [i-2]는 각각 리스트의 끝에 위치한 두 개의 수를 반환한다. 
# 이렇게 반환된 두 수는 합해서 append 함수로 fibonacci 리스트에 추가한다.

