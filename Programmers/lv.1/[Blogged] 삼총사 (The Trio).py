# link :: https://school.programmers.co.kr/learn/courses/30/lessons/131705

# blogged link :: https://medium.com/@va1afar.biz/programmers-coding-test-lv-1-the-trio-2787072bb94


def solution(number):
    answer = 0
    
    first_num = 0
    second_num = 0
    third_num = 0
    
    for i_1 in range(len(number)-2):
        first_num = number[0]
        del number[0]
        for i_2 in range(len(number)-1):
            second_num = number[i_2]
            for i_3 in range(len(number)-(i_2+1)):
                third_num = number[-(i_3+1)]
                if first_num + second_num + third_num == 0:
                    answer += 1
    
    return answer
