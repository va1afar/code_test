# link :: https://school.programmers.co.kr/learn/courses/30/lessons/12985

def solution(n,a,b):
    answer = 1
    
    if a > b: # 計算を簡単にするために、「a」と「b」の中で小さい数を「a」に入れます。
        tmp = b
        b = a
        a = tmp

    # 「a」が奇数で、大きい数が「a」＋１の場合、二人は次のラウンドで出会います。
    # その条件を満足するまでループし、「answer」　＋＝１　します。
    while a % 2 == 0 or (a + b) != (a*2 + 1):
        a = (a // 2) + (a % 2)
        b = (b // 2) + (b % 2)
        answer += 1
    
    return answer