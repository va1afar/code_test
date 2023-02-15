# link :: https://school.programmers.co.kr/learn/courses/30/lessons/120818

def solution(price):
    answer = 0
    
    if price >= 500000:
        price = int(price * 0.8)
    elif price >= 300000:
        price = int(price * 0.9)
    elif price >= 100000:
        price = int(price * 0.95)
        
    answer = price
    
    return answer
