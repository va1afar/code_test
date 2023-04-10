# link :: https://school.programmers.co.kr/learn/courses/30/lessons/120880

def solution(numlist, n):
    answer = []
    
    # 「numlist」の中から一番近い数字を計算し、
    # 「answer」に追加、「numlist」からは削除します。
    #　これを「numlist」の要素が全て無くなるまで繰り返します。
    while len(numlist) > 0:
        closer_num = numlist[0]
        for num in numlist:
            if abs(n - num) < abs(n - closer_num):
                closer_num = num
            elif abs(n - num) == abs(n - closer_num):
                closer_num = max(num, closer_num)
        answer.append(closer_num)
        numlist.remove(closer_num)
        
    return answer