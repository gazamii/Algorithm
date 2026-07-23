def solution(a, b, c, d):
    dice = [a, b, c, d]
    counts = [dice.count(x) for x in dice]
    m = max(counts)

    if m == 4:                    
        return 1111 * a
    if m == 3:                     
        p = dice[counts.index(3)]
        q = dice[counts.index(1)]
        return (10 * p + q) ** 2
    if m == 2 and counts.count(2) == 4:   
        p = dice[0]
        q = [x for x in dice if x != p][0]
        return (p + q) * abs(p - q)
    if m == 2:                     
        q, r = [dice[i] for i in range(4) if counts[i] == 1]
        return q * r
    return min(dice)               