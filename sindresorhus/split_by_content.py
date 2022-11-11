import json

content_list = []
with open("/Users/andrewwonwhoonah/Github-Tag-Embedder/sindresorhus/contents.txt", 'r') as content:
    while True:
        line = content.readline().rstrip()
        if not line:
            break
        content_list.append(line)

output = {}
content_name = ""
item_list = []
line = ""
index = 0

with open('/Users/andrewwonwhoonah/Github-Tag-Embedder/sindresorhus/items_raw.txt', 'r') as f:
    # 제목 순회
    while True:
        line = f.readline()
        if line == content_list[index]:
            content_name = content_list[index]
            continue
        elif line == content_list[index + 1]:
            output[content_name] = item_list
            item_list = []
            index += 1
            if index == len(content_list):
                break
        else:
            item_list.append(line)
            continue
       

with open("/Users/andrewwonwhoonah/Github-Tag-Embedder/sindresorhus/output.json", "w") as json_file:
    json.dump(output, json_file)