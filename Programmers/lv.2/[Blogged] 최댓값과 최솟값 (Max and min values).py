# link :: https://school.programmers.co.kr/learn/courses/30/lessons/12939

# blogged link :: https://medium.com/@va1afar.biz/programmers-coding-test-lv-2-max-and-min-values-c7c1e3acebf2

def solution(s):
    answer = ''
    list_s = []
    cnt = 0     
    
    for i, word in enumerate(s):
        if word == ' ':
            list_s.append(int(s[cnt:i]))
            cnt = i + 1
    list_s.append(int(s[cnt:]))
    answer = str(min(list_s)) + ' ' + str(max(list_s))
    
    return answer