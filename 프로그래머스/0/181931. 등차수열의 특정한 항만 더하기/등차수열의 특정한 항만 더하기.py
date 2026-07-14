def solution(a, d, included):
    answer=0
    for x in range(0,len(included)):
        tlr=d*x+a
        if included[x]:
            answer+=tlr
    return answer