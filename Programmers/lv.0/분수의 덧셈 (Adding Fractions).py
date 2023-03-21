# link :: https://school.programmers.co.kr/learn/courses/30/lessons/120808

def solution(numer1, denom1, numer2, denom2):
    answer = []
    multiple = 0
    lcm = 0
    
    multiple = denom1 * denom2
    while multiple >= 1:
        if multiple % denom1 == 0 and multiple % denom2 == 0:
            lcm = multiple
        multiple -= 1
    
    numer1 = numer1 * (lcm//denom1)
    numer2 = numer2 * (lcm//denom2)
    answer.append(numer1+numer2)
    answer.append(lcm)
    
    gcd = 0
    temp = 1 
    
    while temp <= max(answer[0],answer[1]):
        if answer[0] % temp == 0 and answer[1] % temp == 0:
            gcd = temp
        temp += 1
    if gcd != 0:
        answer[0] = answer[0] // gcd
        answer[1] = answer[1] // gcd
    
    
    
    return answer
