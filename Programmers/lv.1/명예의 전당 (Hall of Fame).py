# link :: https://school.programmers.co.kr/learn/courses/30/lessons/138477

def solution(k, score):
    answer = []
    honor_list = []

    # リストに一個ずつ追加し、その度逆整列するコードです
    for i in score:
        honor_list.append(i)
        honor_list.sort(reverse=True)
        if len(honor_list) < k:
            answer.append(honor_list[-1])
        else:
            answer.append(honor_list[k-1])
    
    return answer