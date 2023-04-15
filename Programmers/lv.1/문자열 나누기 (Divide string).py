# link :: https://school.programmers.co.kr/learn/courses/30/lessons/140108

def solution(s):
    answer = 0
    
    # 最初の文字を「first_str」に保存、「cnt」の初期値を1にした後2番目の文字から「s」に変換しました。
    # ただし、最後まで検査しても「cnt」が0じゃない場合は「s」の文字を削除します。
    
    while len(s) > 0:
        first_str = s[0]
        cnt = 1
        s = s[1:]
        for i in range(len(s)):
            if s[i] == first_str:
                cnt += 1
            else:
                cnt -= 1
            if cnt == 0:
                s = s[i+1:]
                answer += 1
                break
            if i == len(s)-1 :
                s = ""
        if cnt != 0 and len(s) == 0:
            answer += 1

    return answer