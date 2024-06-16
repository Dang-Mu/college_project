# defaultdict : 키가 존재하지 않을 때 자동으로 기본값을 제공하는 딕셔너리
from collections import defaultdict

def readJSON(path):
  for l in open(path, 'r'):
    d = eval(l)
    u = d['userID']
    g = d['gameID']
    yield u,g,d


all_hours = []
user_hours = defaultdict(list)

for uid,gid,d in readJSON("train.json"):
  h = d['hours_transformed']
  all_hours.append(h)
  user_hours[uid].append(h)
  
global_average = sum(all_hours) / len(all_hours)
user_average = {uid: sum(hours) / len(hours) for uid, hours in user_hours.items()}

with open("pairs_Hours.csv", "r") as f1:
    f1.readline() # skip the first row (column names)
    
    with open("hours_answer_example.csv", "w") as f2:
        f2.write("ID,Label\n") # insert the column names at the first row

        for line in f1:
            row_id, uid, gid = line.strip().split(",")
            estimate = user_average[uid] if uid in user_average else global_average
            f2.write(f"{row_id},{estimate}\n")
            
  