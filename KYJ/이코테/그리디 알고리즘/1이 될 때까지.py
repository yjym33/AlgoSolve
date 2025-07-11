# 문제

    # 1이 될 때까지 (기출 : 2018 E 기업 알고리즘 대회) ## (난이도 : 1/3 , 풀이시간 : 30분, 시간제한 : 1초)

    # 어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고 한다.
    # 단, 두번째 연산은 N이 K로 나누어떨어질 때만 선택할 수 있다.

    # 1. N에서 1을 뺀다.
    # 2. N을 K로 나눈다.

    # 예를 들어 N이 17, K가 4라고 가정하자. 이때 1번의 과정을 한 번 수행하면 N은 16이 된다.
    # 이후에 2번의 과정을 두번 수행하면 N은 1이 된다. 결과적으로 이 경우 전체 과정을 실행한 횧수는 3이 된다.
    # 이는 N을 1로 만드는 최소 횟수이다.
    # N과 K가 주어질 때 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 최소 횟수를 구하는 프로그램을 작성하시오.

    # 입력조건 : 첫째 줄에 N(2=<N=<100,000)과 K(2=<K=<100,000)가 공백으로 구분되며 각각 자연수로 주어진다.
    #            이때 입력으로 주어지는 N은 항상 K보가 크거나 같다.

    # 출력조건 : 첫째 줄에 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 횟수의 최솟값을 출력한다.

    # 입력예시 : 25, 5                                출력 예시 : 2

# ---------------------------------------------------------------------------------------------------------------------------
# 풀이1 (단순방법) (Python)

n , k = map(int, input().split())

result = 0

# N이 K 이상이라면 K로 계속 나누기
while n >= k:
    # N이 K로 나누어 떨어지지 않는다면 N에서 1씩 빼기
    while n % k !=0:
        n -= 1
        result += 1
    # K로 나누기
    n //= k
    result += 1

# 마지막으로 남은 수에 대하여 1씩 빼기
while n > 1:
    n -= 1
    result += 1

print(result)
# ---------------------------------------------------------------------------------------------------------------------------
# 풀이2 (효울적인 방법) (Python)
    # N이 100억 이상의 큰 수일때 가정, N이 K의 배수가 되도록 효율적으로 한번에 빼는 방식

# N, K를 공백으로 구분하여 입력받기
n, k = map(int, input().split())
result = 0

while True:
    # (N == K로 나누어떨어지는 수)가 될 때까지 1씩 빼기
    target = (n // k) * k # n이 k로 나누어떨어지지 않을떄, 가장 가까운 K로 나누어 떨어지는 수가 어떤것인지 찾고자 할때 사용
    result += (n-target)
    n = target
    # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # K로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n-1)
print(result)
# ---------------------------------------------------------------------------------------------------------------------------
# 문제 해결 아이디어

# 주어진 N에 대하여 "최대한 많이 나누기"를 수행하면 됩니다.
# N의 값을 줄일 떄, 2 이상의 수로 나누는 작업이 1을 빼는 작업보다 수를 훨씬 많이 줄일 수 있습니다.
# 예를 들어 N = 25, K = 3일떄 
# 25-1 = 24(1단계)
# 24/3 = 8 (2단계)
# 8-1 = 7 (3단계)
# 7-1 = 6 (4단계)
# 6/3 = 2 (5단계)
# 2-1 = 1 (6단계)


