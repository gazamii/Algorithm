def solution(m, i):
    liist=[]
    for x in range(1,len(m)+1):
        liist.append(m[-x:])
    return 1 if i in liist else 0