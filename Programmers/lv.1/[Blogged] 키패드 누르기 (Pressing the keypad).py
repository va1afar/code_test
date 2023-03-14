# link :: https://school.programmers.co.kr/learn/courses/30/lessons/67256

# blogged link :: https://medium.com/@va1afar.biz/programmers-coding-test-lv-1-pressing-the-keypad-be0b0fe07b5


def solution(numbers, hand):
    answer = ''
    Lpos = [0,3]
    Rpos = [2,3]
    key_dict = {1:[0,0], 2:[1,0], 3:[2,0],
                4:[0,1], 5:[1,1], 6:[2,1],
                7:[0,2], 8:[1,2], 9:[2,2],
                         0:[1,3]}
    
    for i in numbers:
        if i == 1 or i == 4 or i == 7:
            answer += 'L'
            Lpos = key_dict[i]
        elif i == 3 or i == 6 or i == 9:
            answer += 'R'
            Rpos = key_dict[i]
        else:
            Ldist = abs(Lpos[0]-key_dict[i][0]) + abs(Lpos[1]-key_dict[i][1]) 
            Rdist = abs(Rpos[0]-key_dict[i][0]) + abs(Rpos[1]-key_dict[i][1])
            if Ldist < Rdist:
                answer += 'L'
                Lpos = key_dict[i]
            elif Ldist > Rdist:
                answer += 'R'
                Rpos = key_dict[i]
            else:
                if hand == 'left':
                    answer += 'L'
                    Lpos = key_dict[i]
                else:
                    answer += 'R'
                    Rpos = key_dict[i]
                    
                
    return answer
