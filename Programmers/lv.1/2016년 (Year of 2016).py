# link :: https://school.programmers.co.kr/learn/courses/30/lessons/12901

def solution(a, b):
    days = [31,29,31,30,31,30,31,31,30,31,30,31]
    weeks = ['FRI',"SAT",'SUN','MON',"TUE",'WED','THU']
    temp = 0
    answer = ''
    
    if a == 1:
        temp = b % 7
        answer = weeks[temp-1]
    else :
        for i in range(a-1):
            temp += days[i]
        temp += b
        temp %= 7
        answer = weeks[temp-1]

    return answer