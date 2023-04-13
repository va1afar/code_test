# link :: https://school.programmers.co.kr/learn/courses/30/lessons/133502

# blogged link :: https://medium.com/@va1afar.biz/programmers-coding-test-lv-1-making-hamburger-e179f54cd4e8

def solution(ingredient):
    answer = 0
    loop = True
    idx = 0
    
    # hamburger must be [1, 2, 3, 1] order.
    # [1, 2, 3, 1]が連続した場合、リストから削除します。
    # 計算するリストがない場合(elif:)while文を停止させます。
    while loop:   
        for i in range(idx, len(ingredient)):
            if ingredient[i:i+4] == [1, 2, 3, 1]:
                answer += 1
                del ingredient[i:i+4]
                idx = i - 2
                break
            elif len(ingredient) - i <= 4:
                loop = False
    
    return answer