# link :: https://school.programmers.co.kr/learn/courses/30/lessons/12945

def solution(n):
    answer = 0
    f_list = []
     
    # 「ｎ」の長さを持つリストを宣言し、計算していきます。
    for i in range(0, n+1):
        if i == 0:
            f_list.append(0)
        elif i == 1:
            f_list.append(1)
        elif i == 2:
            f_list.append(1)
        elif i >= 3:
            f_list.append(f_list[i-2] + f_list[i-1])
    answer = f_list[n] % 1234567    
    
    return answer