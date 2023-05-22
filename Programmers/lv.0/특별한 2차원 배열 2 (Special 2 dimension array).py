# link :: https://school.programmers.co.kr/learn/courses/30/lessons/181831

def solution(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] != arr[j][i]:
                return 0
            
    return 1