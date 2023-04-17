# link :: https://school.programmers.co.kr/learn/courses/30/lessons/120844

def solution(numbers, direction):
    
    if direction == "right":
        numbers.insert(0, numbers.pop())
        return numbers
    else:
        numbers.append(numbers.pop(0))
        return numbers