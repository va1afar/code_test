def solution(n, lost, reserve):
    answer = 0
    cnt = 0
    lost.sort()
    reserve.sort()
    
    # 同じ番号の場合や±１の場合、「reserve」から削除し「cnt」＋1
    # ただ、取られた人が貸してくれる場合もあるので、
    # 「i+1」 の場合その場合をチェックする必要があります。
    for i in lost:
        if i in reserve:
            reserve.remove(i)
            cnt += 1
        elif i-1 in reserve:
            reserve.remove(i-1)
            cnt += 1
        elif i+1 in reserve and i+1 not in lost:
            reserve.remove(i+1)
            cnt += 1
    answer = n - len(lost) + cnt
        
    return answer