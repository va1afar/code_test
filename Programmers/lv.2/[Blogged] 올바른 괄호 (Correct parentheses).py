# link :: https://school.programmers.co.kr/learn/courses/30/lessons/12909

# blogged link :: https://medium.com/@va1afar.biz/programmers-coding-test-lv-2-correct-parentheses-72b6ce5d400

def solution(s):
    answer = True
    stack = []
    
    # '('だけを「stack」に入れ、')'の時一個ずつpop()します。
    for c in s:
        if c == '(':
            stack.append(c)
        else:
            if not stack:
                answer = False
                break
            else:
                stack.pop()
                
    if stack:
        answer = False

    return answer
