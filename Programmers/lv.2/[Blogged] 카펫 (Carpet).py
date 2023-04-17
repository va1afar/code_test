# link :: https://school.programmers.co.kr/learn/courses/30/lessons/42842

# blogged link :: https://medium.com/@va1afar.biz/入出力の例-5dac57930025

def solution(brown, yellow):
    all_blocks = brown + yellow
    row_plus_col = (brown//2) -2
    
    #　*row, colは「yellow」の横縦です*
    # 「brown」は 2*(縦+横+2)なので、縦+横は(「brown」//2 -2)で計算できます。
    #　For文で計算した「縦+横」が複数の可能性もあるので、
    #　全体カーペットの面積でもう一度確認します。
    for col in range(1, row_plus_col):
        row = row_plus_col - col
        if row * col == yellow and (row + 2) * (col + 2) == all_blocks:
                return [(row + 2), (col + 2)]
