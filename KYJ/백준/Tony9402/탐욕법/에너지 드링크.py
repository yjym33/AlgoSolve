# 문제 출처 : https://www.acmicpc.net/problem/20115

N = int(input())
Drink = list(map(int, input().split()))
Drink.sort(reverse=True)
sum_Drink = Drink[0]

for i in range(1, N):
    sum_Drink += Drink[i]/2
print('%g' %sum_Drink)

# 이 문제의 핵심은 
# 에너지 드링크를 내림차순으로 정렬하여 (가장 많은 것부터 순서대로 정렬하기 위해서)
# 가장 양이 많은 드링크를 제외하고 두번쨰부터 양을 반으로 나누어 가장 양이 많은 드링크에 부어주면 되는 것이다.
# 그리고 그대로 출력하게 되면 예시를 기준으로 20.0 소수점 첫번째 자리 까지 출력해버리므로
# 소수점을 제거하기 위해 %g를 사용하여 출력한다.