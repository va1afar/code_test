# link :: https://school.programmers.co.kr/learn/courses/30/lessons/12973

def solution(s):
    answer = -1
    stack = []
    
    #　奇数の場合、必ず余っちゃうので「0」を返還します。
    #　「stack」に1個ずつ入れ、同じ文字が連続した場合削除します。
    #　For文が終わった後、「stack」に何か残ってたらまた「0」を返還します。
    if len(s) % 2 != 0:
        return 0
    
    for i in s:
        stack.append(i)
        if len(stack) >= 2 and stack[-2] == stack[-1]:
            del stack[-2:]
    if stack: 
        return 0
    else:
        return 1