# 회문 문자열 검사

# N개의 문자열 데이터를 입력받아 앞에서 읽을 때나 뒤에서 읽을 때나 같은 경우(회문 문자열)이면 YES를 출력하고 
# 회문 문자열이 아니면 NO를 출력하는 프로그램을 작성한다. 단 회문을 검사할 때 대소문자를 구분하지 않습니다.

# 입력 설명

# 첫 줄에 정수 N(1 <= N <= 20)이 주어지고, 그 다음 줄부터 N개의 단어가 입력된다.
# 각 단어의 길이는 100을 넘지 않는다.

# 출력 설명

# 각 줄에 해당 문자열의 결과를 YES 또는 NO로 출력한다.

# 입력 예제

# 5
# level
# abcba
# soon
# gooG

# 출력 예제 1

#1 YES
#2 NO
#3 YES
#4 NO
#5 YES

# 파이썬스럽게 짠 코드 (손코딩 X)
n = int(input())
for i in range(n):
    s = input()
    s = s.upper()
    if s == s[::-1]:
        print("#%d YES" %(i+1))
    else:
        print("#%d NO" %(i+1))



# 직접 비교하여 비교할 경우 (손코딩 O)
n = int(input())
for i in range(n):
    s = input()
    s = s.upper()
    size = len(s)
    for j in range(size//2):
        if s[j] != s[-1-j]:
            print("#%d NO" %(i+1))
    else:        
        print("#%d YES" %(i+1))
