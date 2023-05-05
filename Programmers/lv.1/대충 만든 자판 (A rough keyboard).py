# link :: https://school.programmers.co.kr/learn/courses/30/lessons/160586

def solution(keymap, targets):
    answer = []
    # 「target」の文字「ch」を「keymap」にあるか検査し、
    # 「cnt_compare」と比較しその中で一番低い数を入れます。
    # 　各「ch」たちの「cnt_compare」を「sum_of_cnt」に追加、全部確認したら「answer」にappendします。
    # 「target」の元素が「keymap」に無かった場合(exist = False)、「ch」の確認を止め「answer」に「-1」をappendします。
    for target in targets:
        sum_of_cnt = 0
        for ch in target:
            cnt_compare = 100
            exist = False
            for key in keymap:
                if ch in key:
                    cnt_compare = min(cnt_compare, key.index(ch)+1)
                    exist = True
            sum_of_cnt += cnt_compare
            if not exist:
                break
        if exist:
            answer.append(sum_of_cnt)
        else:
            answer.append(-1)
                   
    return answer