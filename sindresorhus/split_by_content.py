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
        print(line)
        if not line:
            output[content_name] = item_list
            print(1)
            break
        elif line == content_list[index] + "\n":
            content_name = content_list[index]
            print(2)
            continue
        elif index < len(content_list) - 1 and line == content_list[index + 1] + "\n":
            output[content_name] = item_list
            item_list = []
            index += 1
            content_name = content_list[index]
            print(3)
        else:
            item_list.append(line)
            print(4)
            continue
       

with open("/Users/andrewwonwhoonah/Github-Tag-Embedder/sindresorhus/output.json", "w") as json_file:
    json.dump(output, json_file)