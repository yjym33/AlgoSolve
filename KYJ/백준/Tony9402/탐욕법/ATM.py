https://www.acmicpc.net/problem/11399

N = int(input()) # 사용자가 입력한 값을 변수에 저장
Time = list(map(int, input().split())) # 시간을 리스트로 받아서 저장

Time.sort() # 가장 적은 시간이 드는 순서로 정렬함

Total_Time = 0 # 총시간
Wait_Time = 0 # 대기시간

for i in Time:
    Wait_Time += i # 대기 시간을 누적으로 더한다.
    Total_Time += Wait_Time # 대기 시간을 총시간에 넣어 다음 사람 순서 시간을 반영한다.
    
print(Total_Time) # 출력