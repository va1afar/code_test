# link :: https://school.programmers.co.kr/learn/courses/30/lessons/12950?language=python3

def solution(arr1, arr2):
    answer = []
    
    for i in range(len(arr1)):
        tmp_arr = []
        for j in range(len(arr1[0])):
            tmp_arr.append( arr1[i][j] + arr2[i][j] )
        answer.append(tmp_arr)
            
    return answer


# zip()を使うともっと簡単なコードを書けました
# def sumMatrix(arr1, arr2):
#     answer = [[c + d for c, d in zip(a, b)] for a, b in zip(arr1, arr2)]