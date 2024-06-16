from collections import Counter

def readJSON(path):
  for l in open(path, 'r'):
    d = eval(l)
    u = d['userID']
    g = d['gameID']
    yield u,g,d

game_count = Counter(game for user,game,_ in readJSON("train.json"))
user_count = Counter(user for user,game,_ in readJSON("train.json"))
total_played = sum(game_count.values())
total_users = len(user_count)

return_game_set = set()
return_user_set = set()

count_sum = 0
user_sum = 0

# 게임 카운트를 기준으로 상위 70% 게임 선택
for gid, play_count in game_count.most_common():
    return_game_set.add(gid)
    count_sum += play_count
    if count_sum > total_played * 5 / 10:
        break

# 유저 카운트를 기준으로 상위 50% 유저 선택
for uid, play_count in user_count.most_common():
    return_user_set.add(uid)
    user_sum += 1
    if user_sum > total_users * 1 / 10:
        break


with open("pairs_Played.csv", "r") as f1:
    f1.readline()  # 첫 번째 줄 (열 이름) 건너뛰기

    with open("fifteen_coin.csv", "w") as f2:
        f2.write("ID,Label\n")  # 첫 번째 줄에 열 이름 추가

        for line in f1:
            row_id, uid, gid = line.strip().split(",")
            if gid in return_game_set or uid in return_user_set:
                f2.write(f"{row_id},1\n")
            else:
                f2.write(f"{row_id},0\n")
