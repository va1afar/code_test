# link :: https://school.programmers.co.kr/learn/courses/30/lessons/12915

def solution(strings, n):
    answer = []
    
    for i in range(len(strings)):
        for j in range(i,len(strings)):
            #各要素のn番を比較しスワップ、同じ場合は辞書順にスワップします。
            if strings[i][n] > strings[j][n]: 
                strings[i], strings[j] = strings[j], strings[i]
            elif (strings[i][n] == strings[j][n]) & (strings[i] > strings[j]):
                strings[i], strings[j] = strings[j], strings[i]
                
    answer = strings
    
    return answer