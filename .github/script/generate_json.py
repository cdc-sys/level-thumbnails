import os
import json
f_arr = os.listdir("./thumbs")
content = []
for file in f_arr:
  file_s = str(file)
  file_s2 = file_s.strip(".png")
  content.append(file_s2)
json_dict = {"level_ids":content}
print(json.dumps(json_dict))
