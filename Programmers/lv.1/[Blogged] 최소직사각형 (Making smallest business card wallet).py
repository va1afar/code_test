# link :: https://school.programmers.co.kr/learn/courses/30/lessons/86491

# blogged link :: https://medium.com/@va1afar.biz/programmers-coding-test-lv-1-making-smallest-business-card-wallet-161f3cac1cf9

def solution(sizes):
    answer = 0
    
    list_width = [] #名刺
    list_height = []
    
    
    for i in range(len(sizes)):
        list_width.append(max(sizes[i]))
        list_height.append(min(sizes[i]))
        
    answer = max(list_width)*max(list_height)
    
    return answer
