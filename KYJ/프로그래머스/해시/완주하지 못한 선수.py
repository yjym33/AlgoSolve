# 수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.
# 마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때,
# 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

# 제한사항
# 마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
# completion의 길이는 participant의 길이보다 1 작습니다.
# 참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
# 참가자 중에는 동명이인이 있을 수 있습니다.

# 입출력 예
# participant	    completion	    return
# [leo, kiki, eden]	[eden, kiki]	leo
# [marina, josipa, nikola, vinko, filipa]	[josipa, filipa, marina, nikola]	vinko
# [mislav, stanko, mislav, ana]	[stanko, ana, mislav]	mislav

# 입출력 예 설명
# 예제 #1
# leo는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.

# 예제 #2
# vinko는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.

# 예제 #3
# mislav는 참여자 명단에는 두 명이 있지만, 완주자 명단에는 한 명밖에 없기 때문에 한명은 완주하지 못했습니다.


# 풀이
import collections


def solution(participant, completion):

    # 동명이인이 없는 경우 : 참가자에서 완주자 빼주기 (중복제거)
    complement = list(set(participant) - set(completion))

    if len(complement) != 0:
        return complement[0]

    # 동명이인이 있는 경우 (정렬후 인덱스를 돌며 비교해서 다르면 해당하는 participant[i] 출력)
    participant = sorted(participant)
    completion = sorted(completion)

    for i in range(len(participant)):
        if participant[i] != completion[i]:
            return participant[i]

    answer = ''
    return answer


# 다른 사람 풀이


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.key[0])

# Collection.Counter 사용법 참고
# https://m.blog.naver.com/PostView.nhn?blogId=wideeyed&logNo=221540885097&proxyReferer=https:%2F%2Fwww.google.com%2F
# https://velog.io/@oaoong/Python-collections%EB%AA%A8%EB%93%88-Counter
