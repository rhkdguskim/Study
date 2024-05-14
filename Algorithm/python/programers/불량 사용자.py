def solution(user_id, banned_id):
    def is_match(user, ban):
        if len(user) != len(ban):
            return False
        for i in range(len(user)):
            if ban[i] != '*' and user[i] != ban[i]:
                return False
        return True
    
    # 각 banned_id에 대응하는 가능한 user_id 목록을 만듦
    possible_users = []
    for ban in banned_id:
        matching_users = set()
        for user in user_id:
            if is_match(user, ban):
                matching_users.add(user)
        possible_users.append(matching_users)
    
    def dfs(index, selected):
        if index == len(possible_users):
            result.add(tuple(sorted(selected)))
            return
        for user in possible_users[index]:
            if user not in selected:
                selected.add(user)
                dfs(index + 1, selected)
                selected.remove(user)
    
    result = set()
    dfs(0, set())
    
    return len(result)