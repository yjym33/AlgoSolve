# 문제

# 예제 3-1 (거스름돈)

# 당신은 음식점의 계산을 도와주는 점원이다. 카운터에는 거스름돈으로 사용할 500원, 100원 50원, 10원짜리 동전이 무한히 존재한다고 가정한다.
# 손님에게 거슬러 줘야 할 돈이 N원일 때 거슬러 줘야 할 동전의 최소개수를 구하여라.
# (단 거슬러 줘야 할 돈 N은 항상 10의 배수이다.)

# -------------------------------------------------------------------------------------------------------------------------
# 풀이 (Python)

n = 1260
count = 0

# 큰 단위의 화폐부터 차례대로 확인
list = [500, 100, 50, 10]

for coin in list:
    count += n // coin  # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin

print(count)

# -------------------------------------------------------------------------------------------------------------------------
# 문제해설

# 이 문제는 그리디 알고리즘을 이용해 풀 수 있는 대표적인 문제로 간단한 아이디어만 떠올릴수 있으면 문제를 해결할 수 있다.
# 그것은 바로 “ 가장 큰 화폐 단위부터 ” 돈을 거슬러 주는 것이다.
# N원을 거슬러 줘야 할때, 가장 먼저 500원으로 거슬러 줄 수 있을 만큼 거슬러 준다.
# 그다음 100원, 50원, 10원 짜리 동전을 차례대로 거슬러 줄수 있을 만큼 거슬러 주면 최소의 동전 개수로 모두 거슬러 줄수 있다.

# EX) 입력으로 주어진 N 이 1260원이라고 가정해보자

# STEP 0
#  초기단계 - 남은 돈 1,260원 (아무것도 나누어주지 않은 상태)

# STEP 1
#  남은돈 260원 : 1,260 원에서 500 원 짜리로 거슬러줄수 있는 돈은 1,000원, 즉 500원 2개이고 남은 돈은 260원이다.

# STEP 2
#  남은돈 60 원 : 앞 단계에서 남은 돈 260원 에서 100원 단위로 거슬러 줄수 있는 돈은 200원, 즉 100원 2개이고 남은돈은 60원이다.

# STEP 3
#  남은돈 10 원 : 역시 앞 단계에서 남은 돈 60원에서 50원 단위로 거슬러 줄수 있는 돈은 1개이고, 남은 돈은 10원이다.

# STEP 4
#  남은돈 0원 : 이제 남은 돈은 10원이고, 10원 1개를 거슬러 주며 거스름돈 계산을 모두 마쳤다.

# 따라서 손님이 받은 동전의 최소 개수는 6개이다.

# 정당성 분석 : 가장 큰 화폐 단위부터 돈을 거슬러 주는 것이 최적의 해를 보장하는 이유는 무엇일까요?
#               가지고 있는 동전 중에서 큰 단위가 항상 작은 단위의 배수이므로 작은 단위의 동전들을 종합해 다른 해가 나올수 없기 떄문입니다.
#
