def recursive_function(i):
    # 100번째 출력했을 때 종료되도록 종료 조건 명시
    if i == 100:
        return

    print(i, '번째 재귀 함수에서', i+1, '번째 재귀 함수를 호출합니다.')
    recursive_function(i + 1)
    print(i, '번쨰 재귀 함수를 종료합니다.')

recursive_function(1)

# 재귀 함수는 내부적으로 스택 자료구조와 동일하다. 
# 따라서 스택 자료구조를 활용해야 하는 상당수 알고리즘은 재귀 함수를 이용해 간편하게 구현될 수 있다. DFS가 대표적인 예이다.
# 재귀 함수를 이용하는 대표적인 예제로는 팩토리얼(Factorial) 문제가 있다.