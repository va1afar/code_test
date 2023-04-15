# link :: https://school.programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    answer = 0
    stack = []
    
    # 効率的な計算のために、「board」の内部リストで「moves」に該当する要素だけを計算します。
    # 「stack」に追加する度に、同じ人形が連続したら2つを消し、「answer」+= 2 します。
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] != 0:
                stack.append(board[i][move-1])
                board[i][move-1] = 0
                if len(stack) >= 2 and stack[-1] == stack[-2]:
                    del stack[-2:]
                    answer += 2   
                break
    
    return answer