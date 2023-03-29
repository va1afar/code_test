# link :: https://school.programmers.co.kr/learn/courses/30/lessons/42889

# blogged link :: https://medium.com/@va1afar.biz/2019-kakao-ブラインド採用-programmers-coding-test-lv-1-failure-rate-d48ee7becc17

def solution(N, stages):
    answer = []
    fail_rate = []
    failed = 0
    reached = 0
    
    # for文で失敗率を計算し、fail_rateに2次元リストの形で保存します。
    # その後、sorted()を使って失敗率の高い順から優先的に整列、
    # 同じ場合は正順で整列しました。
    for i in range(1, N+1):
        for j in stages:
            if i == j:
                failed += 1
            if i <= j:
                reached += 1
        if reached == 0:
            fail_rate.append([i, 0.0])
        else:
            fail_rate.append([i, failed/reached])
        reached, failed = 0, 0           

    tmp = sorted(fail_rate, key=lambda x: x[1], reverse=True)
    
    for i in range(len(tmp)):
        answer.append(tmp[i][0])
    
    
    return answer