# link :: https://school.programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    answer = 0
    citations.sort()

    for i in range(len(citations)):
        if citations[i] > len(citations)-i:
            if answer == 0:
                answer = min(citations[i], len(citations))
            break
        elif max(citations[i], len(citations)-(i+1)) >= i+1: 
            if citations[i] != citations[i-1]: # 重複した元素の場合、最初の元素のみ計算するためです。
                answer = max(citations[i], len(citations)-(i+1))
            else:
                continue

    return answer