# 기출 Facebook 인터뷰 , 난이도 : 1/3

# 알파벳 대문자와 숫자(0 ~ 9)로만 구성된 문자열이 입력으로 주어집니다.
# 이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에, 그 뒤에 모든 숫자를 더한 값을 이어서 출력합니다.
# 예를 들어 K1KA5CB7이라는 값이 들어오면 ABCKK13을 출력합니다.

# 입력 조건 : 첫째 줄에 하나의 문자열 S가 주어집니다. (1 =< S의 길이 =< 10,000)
# 출력 조건 : 첫째 줄에 문제에서 요구하는 정답을 출력합니다.

# 입력 예시 1 : K1KA5CB7          출력 예시 : ABCKK13
# 입력 예시 2 : AJKDLSI412K4JSJ9D 출력 예시 : ADDIJJJKKLSS20

# ---------------------------------------------------------------------------------------------------------------------------
# 풀이 (Python)

data = input()
result = []
value = 0

# 문자를 하나씩 확인하며
for x in data:
    # 알파벳인 경우 결과 리스트에 삽입
    if x.isalpha():
        result.append(x)
        # 숫자는 따로 더하기
    else:
        value += int(x)

# 알파벳을 오름차순으로 정렬
result.sort()

# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value != 0:
    result.append(str(value))

# 최종 결과 출력(리스트를 문자열로 변환하여 출력)
print("".join(result))
# join에서 (""는 구분자, 구분자를 기준으로 문자열을 붙임)
# ---------------------------------------------------------------------------------------------------------------------------

# 요구사항대로 충실히 구현하면 되는 문제입니다.
# 문자열이 입력되었을 때 문자를 하나씩 확인합니다.
# 숫자인 경우 따로 합계를 계산합니다.
# 알파벳의 경우 별도의 리스트에 저장합니다.
# 결과적으로 리스트에 저장된 알파벳을 정렬해 출력하고, 합계를 뒤에 붙여 출력
