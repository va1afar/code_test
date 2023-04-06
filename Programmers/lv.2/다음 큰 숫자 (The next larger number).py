# link :: https://school.programmers.co.kr/learn/courses/30/lessons/12911

def solution(n):
    answer = 0
    answer_tmp = ''
    binary_n = '0' + str(format(n,'b'))
    point = 0
    
    # 0の次に1がくる位置の中で一番右を「point」に保存
    for i in range(len(binary_n)-1):
        if binary_n[i] == '0' and binary_n[i+1] == '1':
            point = i
    
    # iとi+1の位置を変えながら、その後の数字たちを正順で整列し追加します。
    answer_tmp = binary_n[:point] + '10' +''.join(sorted(binary_n[point+2:]))
    answer = int(answer_tmp, 2)
    
    return answer