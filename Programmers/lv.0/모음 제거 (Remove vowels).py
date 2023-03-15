# link :: https://school.programmers.co.kr/learn/courses/30/lessons/120849

def solution(my_string):
    answer = ''
    vowel_list = ['a','e','i','o','u']

    for i in my_string:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i =='u':
            continue
        else:
            answer += i
            
    return answer