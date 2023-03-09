# link :: https://school.programmers.co.kr/learn/courses/30/lessons/131705

# blogged link :: https://medium.com/@va1afar.biz/programmers-coding-test-lv-1-the-trio-2787072bb94

# simpler solution :: https://medium.com/@va1afar.biz/programmers-coding-test-lv-1-the-trio-%E3%81%AE%E3%82%88%E3%82%8A%E7%B0%A1%E5%8D%98%E3%81%AA%E8%A7%A3%E6%B3%95-7465d58930db


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
