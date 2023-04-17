# link :: https://school.programmers.co.kr/learn/courses/30/lessons/120895

def solution(my_string, num1, num2):
    answer = ""
    list_str = list(my_string)
    
    list_str[num1], list_str[num2] = list_str[num2], list_str[num1]
    answer = "".join(map(str,list_str))
    
    return answer