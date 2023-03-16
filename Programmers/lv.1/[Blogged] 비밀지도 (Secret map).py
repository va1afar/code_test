# link :: https://school.programmers.co.kr/learn/courses/30/lessons/17681

# blogged link :: https://medium.com/@va1afar.biz/2018-kakao-ブラインド採用-programmers-coding-test-lv-1-secret-map-82507f3ac550

def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        # 0bを含まず、長さがnで固定されるbin(arr1[i]|arr2[i])をanswerに入れます。
        answer.append( format(arr1[i] | arr2[i], 'b').zfill(n) )
        answer[i] = answer[i].replace('1','#').replace('0',' ')
    
    return answer