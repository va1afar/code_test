# link :: https://school.programmers.co.kr/learn/courses/30/lessons/134240

# blogged link :: https://medium.com/@va1afar.biz/programmers-coding-test-lv-1-a-food-fight-competition-b998915a250b

def solution(food):
    # variable
    answer = ''
    i = 1
    
    # calc.
    food.pop(0)
    for each_food in food:
        answer += (str(i) * (each_food//2))
        i += 1
    answer = answer + '0' + answer[::-1]
    
    return answer
