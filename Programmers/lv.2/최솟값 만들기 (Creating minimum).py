# link :: https://school.programmers.co.kr/learn/courses/30/lessons/12941

def solution(A,B):
    answer = 0
    
    # Ａは正順、Ｂは逆順で整列し、最小ｘ最大になるようコードです。
    A.sort()
    B.sort(reverse = True)
    for i in range(len(A)):
        answer += A[i] * B[i]
    
    return answer