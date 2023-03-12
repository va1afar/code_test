# link :: https://school.programmers.co.kr/learn/courses/30/lessons/68935

def solution(n):
    answer = 0
    triad_n = ''
    
    # Converting from Decimal(int) to Triad(str)
    while n >= 1:
        triad_n += str(n % 3)  
        n = n // 3
        
    # Flip triad, re-convert Triad to Decimal
    triad_n = triad_n[::-1]
    for i, word in enumerate(triad_n):
        if i == 0:
            answer += int(triad_n[i])
        else:
            answer += int(triad_n[i]) * (3**i) 
            
    return answer


# より簡単な解決方法
# def solution(n):
#     answer = ''
#     
#     while n >= 1:
#         n, rest = divmod(n, 3)
#         answer += str(rest)
#     answer = int(answer, 3)
#     
#     return answer
