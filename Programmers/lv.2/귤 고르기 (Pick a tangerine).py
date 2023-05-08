# link :: https://school.programmers.co.kr/learn/courses/30/lessons/138476

from collections import Counter

def solution(k, tangerine):
    answer = 0
    cnt_tangerine = Counter(tangerine) # tangerineの各元素の数を計算します。
    
    for size, num in cnt_tangerine.most_common(): # 数の多い順で作動させます。
        if k >= 1:
            k -= num
            answer += 1
        else:
            break
    
    return answer