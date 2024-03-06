import os

f_arr = os.listdir("./thumbs")
content = []
for file in f_arr:
  file_s = str(file)
  file_s2 = file_s.strip(".png")
  content.append(file_s2)
print(content)
