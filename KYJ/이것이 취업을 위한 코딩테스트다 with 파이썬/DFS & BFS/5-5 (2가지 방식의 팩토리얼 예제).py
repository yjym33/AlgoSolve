# 반복적으로 구현한 n!
def factorial_iterative(n):
    result = 1
    # 1부터 n까지의 수를 차례대로 곱하기
    for i in range(1, n+1):
        result *= i
    return result

# 재귀적으로 구현한 n!
def factorial_recursive(n):
    if n <= 1:  # n이 1 이하인 경우 1을 반환
        return 1
    # n! = n * (n-1)!를 그대로 코드로 작성하기
    return n * factorial_recursive(n-1)

# 각각의 방식으로 구현한 n! 출력(n = 5)
print('반복적으로 구현:', factorial_iterative(5))
print('재귀적으로 구현:', factorial_recursive(5))

# 두 실행 결과는 동일하지만, 재귀 함수의 코드가 반복적으로 구현한 함수보다 코드가 더 간결하다.
# 수학의 점화식(재귀식)을 그대로 소스코드로 옮겼기 때문이다.
# 수학에서 점화식은 특정한 함수를 자신보다 더 작은 변수에 대한 함수와의 관계로 표현한 것을 의미한다. (**다이나믹 프로그래밍으로 이어지기 때문에 중요**)

    # 팩토리얼을 수학적 점화식으로 표현해보면 다음과 같다
    #   n이 0 혹은 1일 때 : Factorial(n)=1
    #   n이 1보다 클 때 : Factorial(n)= n x Factorial(n-1)
    