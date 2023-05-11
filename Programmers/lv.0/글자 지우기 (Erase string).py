# link :: https://school.programmers.co.kr/learn/courses/30/lessons/181900

def solution(my_string, indices):
    indices.sort(reverse=True)
    
    for i in indices:
        my_string = my_string[:i] + my_string[i+1:]
    
    return my_string