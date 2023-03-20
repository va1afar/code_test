# link :: https://school.programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    answer = []
    
    for i in commands:
        # tmpにarray[i:j]を入力、整列しtmp[k]をanswerを追加します。
        tmp = ( array[i[0]-1:i[1]] ) 
        tmp.sort()
        answer.append(tmp[i[2]-1])
    
    return answer