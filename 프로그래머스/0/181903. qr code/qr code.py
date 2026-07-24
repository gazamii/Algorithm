def solution(q, r, code):
    answer = []
    for x in range(0, len(code)):
        if x%q==r:
            answer.append(code[x])
    return "".join(answer)
    