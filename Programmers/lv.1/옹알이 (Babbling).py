# link :: https://school.programmers.co.kr/learn/courses/30/lessons/133499

def solution(babbling):
    answer = 0
    
    # 該当する場合「point」で次のアルファベットを指定、「point」が「babble」の長さになるまで繰り返します。
    # 1個も該当しない場合はbreakで次の「babble」に移動します。
    # 連続する場合は無効なので、「former_word」と連続しない場合のみを計算します。
    for babble in babbling:
        point = 0
        former_word = ""
        while point < len(babble):
            if babble[point:point+3] == "aya" and former_word != "aya":
                point += 3
                former_word = "aya"
            elif babble[point:point+2] == "ye" and former_word != "ye":
                point += 2
                former_word = "ye"
            elif babble[point:point+3] == "woo" and former_word != "woo":
                point += 3
                former_word = "woo"
            elif babble[point:point+2] == "ma"  and former_word != "ma":
                point += 2
                former_word = "ma"
            else:
                break
        if point == len(babble):
            answer += 1
    
    return answer