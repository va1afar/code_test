# link :: https://school.programmers.co.kr/learn/courses/30/lessons/42885

# blogged link :: https://medium.com/@va1afar.biz/programmers-coding-test-lv-2-resque-boat-a031b6e0eca1

from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    p_deq = deque(people)
    
    # 「people」を整列し、dequeリスト化します。
    # 最高体重＋最低体重<=「limit」の場合、両方を削除
    # それ以外は最大重さだけど削除するコードになります。
    while p_deq:
        if p_deq[-1] + p_deq[0] <= limit and len(p_deq) >= 2:
            p_deq.pop()
            p_deq.popleft()
            answer += 1
        else:
            p_deq.pop()
            answer += 1
    
    return answer