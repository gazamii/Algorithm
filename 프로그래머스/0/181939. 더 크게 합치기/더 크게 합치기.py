def solution(a, b):
    answer = 0
    answer=str(a)+str(b)
    if answer>(str(b)+str(a)):
         answer=int(answer)
    else :
        answer=str(b)+str(a)
        answer=int(answer)
    return answer