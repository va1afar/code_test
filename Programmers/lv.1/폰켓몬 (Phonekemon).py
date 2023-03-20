# link :: https://school.programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    answer = 0
    got_pkm = []
    
    for i in nums: 
        if i not in got_pkm: #numsの要素が無い時のみ追加します。
            got_pkm.append(i)
    answer = len(got_pkm) #全体種類の数
    if len(got_pkm) > len(nums) // 2: #ただ、その数はnums//2を越えられない
        answer = len(nums) // 2
    
    return answer