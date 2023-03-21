# link :: https://school.programmers.co.kr/learn/courses/30/lessons/12940

# blogged link :: https://medium.com/@va1afar.biz/programmers-coding-test-lv-1-gcd-and-lcm-8cd64071d176

def solution(n, m):
    answer = []
    # どっちの数が大きいか分からないため、確認します。
    max_num = max(n, m)
    min_num = min(n, m)
    
    # ユークリッドの互除法を使います。
    while min_num != 0:
        [max_num, min_num] = [min_num, max_num % min_num]
    answer.append(max_num) # GCD
    answer.append(n * m / max_num) # LCM
        
    return answer