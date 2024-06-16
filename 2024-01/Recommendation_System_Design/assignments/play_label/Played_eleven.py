from collections import Counter

def readJSON(path):
  for l in open(path, 'r'):
    d = eval(l)
    u = d['userID']
    g = d['gameID']
    yield u,g,d

game_count = Counter(game for user,game,_ in readJSON("train.json"))
total_played = sum(game_count.values())

return_set = set()
count_sum = 0
for gid, play_count in game_count.most_common():
    return_set.add(gid)
    count_sum += play_count
    if count_sum > total_played*71/100: break

with open("pairs_Played.csv", "r") as f1:
    f1.readline() # skip the first row (column names)
    
    with open("eleven_coin.csv", "w") as f2:
        f2.write("ID,Label\n") # insert the column names at the first row

        for line in f1:
            row_id, uid, gid = line.strip().split(",")
            f2.write(f"{row_id},{1 if gid in return_set else 0}\n")
            
                

