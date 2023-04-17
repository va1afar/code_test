# link :: https://school.programmers.co.kr/learn/courses/30/lessons/12981

def solution(n, words):
    used = []
    last_alpha = words[0][0]
    
    # 脱落者=「ｎ」の場合、脱落者の番号が「0」になっちゃうので、
    # 脱落者=「ｎ」の場合とそうじゃない場合に分け、計算します。
    for i in range(len(words)):
        if last_alpha != words[i][0] or words[i] in used:
            if (i+1) % n == 0:
                return [n, (i+1)//n]
            else:
                return [(i+1)%n, (i+1)//n +1]
        else:
            used.append(words[i])
            last_alpha = words[i][-1]
            
    return [0, 0]