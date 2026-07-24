def solution(my_string, is_prefix):
    liist=[]
    for n in range(1, len(my_string)+1):
        liist.append(my_string[:n])
    return 1 if is_prefix in liist else 0