def recursive_function():
    print("재귀 함수를 호출합니다.")
    recursive_function()

recursive_function()

# 재귀 함수는 자기 자신을 다시 호출하는 함수를 의미합니다.

# 재귀 함수를 호출합니다. 문자열 무한히 출력후, 다음과 같은 오류메세지 출력
# RecursionError : maximum recursion depth exceeded while pickling an object
# 이 오류메세지는 재귀의 최대 깊이를 초과했다는 내용이다. 
# 보통 파이썬 인터프리터는 호출 횟수 제한이 있는데 이 한계를 벗어났기 때문이다. 따라서 무한대로 재귀 호출을 진행할 수는 없다.