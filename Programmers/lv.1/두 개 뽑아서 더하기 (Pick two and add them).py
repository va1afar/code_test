# link :: https://school.programmers.co.kr/learn/courses/30/lessons/68644

def solution(numbers):
    answer = []
    
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)): #iとjが被らないように設定
            if numbers[i]+numbers[j] not in answer:
                answer.append(numbers[i] + numbers[j])
            else:
                continue
            
    answer.sort()
    
    return answer