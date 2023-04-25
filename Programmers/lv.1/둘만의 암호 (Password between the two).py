# link :: https://school.programmers.co.kr/learn/courses/30/lessons/155652

def solution(s, skip, index):
    answer = ""
    
    alpha = "abcdefghijklmnopqrstuvwxyz" 
    
    for i in list(skip): 
        if i in alpha:
            alpha = alpha.replace(i, "") # 「alpha」の中から「skip」の要素を削除します。
    
    for j in s:
        change = alpha[(alpha.find(j) + index) % len(alpha)] # 「alpha」の中で「index」の分後ろの文字にします。
        answer += change
    
    return answer