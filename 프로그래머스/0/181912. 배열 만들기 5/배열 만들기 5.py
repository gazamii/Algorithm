def solution(intStrs, k, s, l):
    result=[]
    for x in intStrs:
        answer = []
        x=list(x)
        for a in range(s,s+l):
            answer.append(x[a])
        answer=int("".join(answer))
        if answer>k:
            result.append(answer)
    return result
