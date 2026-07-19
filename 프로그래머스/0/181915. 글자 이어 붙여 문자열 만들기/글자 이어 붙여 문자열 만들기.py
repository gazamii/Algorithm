def solution(m, i):
    answer = []
    m=list(m)
    for n in i:
        answer.append(m[n])
    return "".join(answer)