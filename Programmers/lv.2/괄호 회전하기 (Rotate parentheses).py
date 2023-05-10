# link :: https://school.programmers.co.kr/learn/courses/30/lessons/76502

# blogged link :: 

def solution(s):
    answer = 0
    
    for rotate in range(0, len(s)):
        stack_small = [] # ()
        stack_middle = [] # []
        stack_big = [] # {}
        stack_last = [] # 括弧の左側を保存、「({)}」のような場合を排除するため使用。
        succeed = True # 途中に失敗したか確認。
        
        # 各stackが正しい括弧になっているか確認。
        for i in range(0, len(s)):
            if s[i] == '(':
                stack_small.append(s[i])
                stack_last.append(s[i])
            elif s[i] == ')':
                if (not stack_small) or stack_last[-1] != '(':
                    succeed = False
                    break
                else:
                    stack_small.pop()
                    stack_last.pop()

            elif s[i] == '[':
                stack_middle.append(s[i])
                stack_last.append(s[i])
            elif s[i] == ']':
                if (not stack_middle) or stack_last[-1] != '[':
                    succeed = False
                    break
                else:
                    stack_middle.pop()
                    stack_last.pop()

            elif s[i] == '{':
                stack_big.append(s[i])
                stack_last.append(s[i])
            elif s[i] == '}':
                if (not stack_big)  or stack_last[-1] != '{':
                    succeed = False
                    break
                else:
                    stack_big.pop()
                    stack_last.pop()

        # 最後まで正しい括弧の場合、answer += 1
        if succeed and (len(stack_small) + len(stack_middle) + len(stack_big) == 0):
            answer += 1
            
        # リスト「s」を回転。
        s = s[1:] + s[0]
        
    
    return answer