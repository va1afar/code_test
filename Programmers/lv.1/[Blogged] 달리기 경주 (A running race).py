# link :: https://school.programmers.co.kr/learn/courses/30/lessons/178871

# blogged link :: https://medium.com/@va1afar.biz/programmers-coding-test-lv-1-a-running-race-54d2dcda78e7

def solution(players, callings):
    # 名前：順位のdict宣言。
    name_idx_dict = {name : i for i, name in enumerate(players)}
    # 順位：名前のdict宣言。
    idx_name_dict = {i : name for i, name in enumerate(players)}
    
    for call in callings:
        # 呼ばれた名前と追い越す名前、そして両方の順位も計算します。
        current_idx = name_idx_dict[call]
        overtake_idx = current_idx - 1
        current_name = call
        overtake_name = idx_name_dict[overtake_idx]
        # 順位を切り替えます。
        name_idx_dict[current_name] = overtake_idx
        name_idx_dict[overtake_name] = current_idx
        # 名前を切り替えます。
        idx_name_dict[current_idx] = overtake_name
        idx_name_dict[overtake_idx] = current_name
        
    return list(idx_name_dict.values()) # 順位順番通り返還します。