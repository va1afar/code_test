# link :: https://school.programmers.co.kr/learn/courses/30/lessons/120884

def solution(chicken):
    answer = 0
    coupon = 0
    
    while chicken >= 10:
        coupon = chicken // 10
        answer += coupon
        chicken = coupon + (chicken % 10)
        coupon = 0
    
    return answer