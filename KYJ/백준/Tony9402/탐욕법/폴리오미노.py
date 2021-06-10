# https://www.acmicpc.net/problem/1343

po = input()

# replace는 왼쪽부터 해당하는 문자열을 찾아서 치환한다.
po = po.replace('XXXX', 'AAAA') # 왼쪽부터 XXXX를 찾아서 AAAA로 치환한다.
po = po.replace('XX', 'BB') # 왼쪽부터 XX를 찾아서 BB로 치환한다.

if 'X' in po:
    print(-1) # 치환하고 난후 X가 보드판에 남아있다면 X 보드판을 폴리오미노로 덮을수 없는 것
else:
    print(po)


