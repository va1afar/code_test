# link :: https://school.programmers.co.kr/learn/courses/30/lessons/142086

# blogged link :: https://medium.com/@va1afar.biz/programmers-coding-test-lv-1-the-nearest-same-letter-2ea9e34fce8d

def solution(s):
    answer = []
    word_dict = {}
    
    for num, word in enumerate(list(s)):
        if word in word_dict:
            answer.append(num - word_dict[word])
            word_dict[word] = num
        else:
            answer.append(-1)
            word_dict[word] = num
 
    return answer
