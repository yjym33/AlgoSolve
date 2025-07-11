# 볼링공 고르기

# A, B 두 사람이 볼링을 치고 있습니다.
# 두 사람은 서로 무게가 다른 볼링공을 고르려고 합니다.
# 볼링공은 총 N개가 있으며 각 볼링공마다 무게가 적혀 있고, 공의 번호는 1번부터 순서대로 부여됩니다.
# 또한 같은 무게의 공이 여러개 있을 수 있지만, 서로 다른 공으로 간주합니다. 볼링공의 무게는 1부터 M까지의 자연수 형태로 존재합니다.

# 예를 들어 N이 5이고, M이 3이며 각각의 무게가 차례대로 1, 3, 2, 3, 2 일때 각 공의 번호가 차례대로 1번부터 5번까지 부여됩니다.
# 이때 두 사람이 고를 수 있는 볼링공 번호의 조합을 구하면 다음과 같습니다.

# (1번, 2번), (1번, 3번), (1번, 4번), (1번, 5번), (2번, 3번), (2번, 5번), (3번, 4번), (4번, 5번)

# 결과적으로 두 사람이 공을 고르는 경우의 수는 8가지 입니다. N개의 공의 무게가 각각 주어질 때,
# 두 사람이 볼링공을 고르는 경우의 수를 구하는 프로그램을 작성하세요.

# 입력조건 : 첫째 줄에 볼링공의 개수 N, 공의 최대 무게 M이 공백으로 구분되어 각각 자연수 형태로 주어집니다.
#          (1 =< N =< 1,000, 1 =< M =< 10)
#          둘째 줄에 각 볼링공의 무게 K가 공백으로 구분되어 순서대로 자연수 형태로 주어집니다.
#          (1 =< K =< M)

# 출력조건 : 첫째 줄에 두 사람이 볼링공을 고르는 경우의 수를 출력합니다.

# 입력 예시 1 : 5 3                                             출력 예시 1 : 8
#             1 3 2 3 2


# 문제 해결 방법

#   1. 이 문제를 해결하기 위해서는 먼저 무게마다 볼링공이 몇개 있는지를 확인한다.
#   2. 이때 A가 특정한 무게의 볼링공을 선택했을 때, 이어서 B가 볼링공을 선택하는 경우를 차례대로 계산하여 문제를 해결할 수 있다.
#       A를 기준으로 무게가 낮은 볼링공 부터 무게가 높은 볼링공 까지 순서대로 하나씩 확인한다고 했을 때 다음과 같다

#       Step 1 : A가 무게가 1인 공을 선택할 떄의 경우의 수는
#       1(무게가 1인 공의 개수) X 4(B가 선택하는 경우의 수) = 4가지 경우
#       Step 2 : A가 무게가 2인 공을 선택할 때의 경우의 수는
#       2(무게가 2인 공의 개수) X 2(B가 선택하는 경우의 수) = 4가지 경우
#       Step 3 : A가 무게가 3인 공을 선택할 떄의 경우의 수는
#       2(무게가 3인 공의 개수) X 0(B가 선택하는 경우의 수) = 0가지 경우

# 따라서 가능한 경우의 수는 총 8가지이다

# (1번, 2번), (1번, 3번), (1번, 4번), (1번, 5번), (2번, 3번), (2번, 5번), (3번, 4번), (4번, 5번)

# 풀이

n, m = map(int, input().split())
data = list(map(int, input().split()))

# 1부터 10까지의 무게를 담을 수 있는 리스트
array = [0] * 11

for x in data:
    # 각 무게에 해당하는 볼링공의 개수 카운트
    array[x] += 1

result = 0
# 1부터 m까지의 각 무게에 대하여 처리
for i in range(1, m+1):
    n -= array[i]  # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수)제외
    result += array[i] * n  # B가 선택하는 경우의 수와 곱하기

print(result)
