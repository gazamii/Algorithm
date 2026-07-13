def solution(code):
    mode = 0
    ret = ''
    for i, x in enumerate(code):
        if x == '1':
            mode = 1 - mode
        else:
            if mode == 0:
                if i % 2 == 0:
                    ret += x
            elif mode == 1:
                if i % 2 == 1:
                    ret += x
    if ret == '':
        return 'EMPTY'
    return ret