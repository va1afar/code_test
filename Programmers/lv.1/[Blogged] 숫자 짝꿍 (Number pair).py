# link :: https://school.programmers.co.kr/learn/courses/30/lessons/131128

# blogged link :: https://medium.com/@va1afar.biz/programmers-coding-test-lv-1-number-partner-9c1bbe530e9c

from collections import Counter

def solution(X, Y):
    answer = ''
    
    # 各数字のカウントをdict形式で保存します。
    # ex) {'1': 0, '2': 3, ....}
    cnt_X = Counter(X)
    cnt_Y = Counter(Y)
    
    # 0から9まで比較、どっちも1個以上ある場合if文が発動
    # そして重なる分を「answer」に入力
    for i in range(0, 10):
        if cnt_X[str(i)] != 0 and cnt_Y[str(i)] != 0:
            answer += str(i) * min(cnt_X[str(i)], cnt_Y[str(i)])
            
    # 「answer」を逆順で整列します、
    # ただ、全部０の場合「０」一個で、何もない場合「－1」を返還
    answer = ''.join(sorted(answer,reverse=True))
    if answer == '':
        answer = '-1'
    elif answer[0] == '0':
        answer = '0'
    
    return answer