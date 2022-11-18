import json

content_list = []
with open("/Users/andrewwonwhoonah/Github-Tag-Embedder/sindresorhus/Machine_Learning/3_contents_1.txt", 'r') as content:
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

with open('/Users/andrewwonwhoonah/Github-Tag-Embedder/sindresorhus/Machine_Learning/2_refined_1.txt', 'r') as f:
    # 제목 순회
    while True:
        line = f.readline()
        # print(line)
        if not line:
            output[content_name] = item_list
            # print(1)
            break
        elif line == content_list[index] + "\n":
            content_name = content_list[index]
            # print(2)
            continue
        elif index < len(content_list) - 1 and line == content_list[index + 1] + "\n":
            output[content_name] = item_list
            item_list = []
            index += 1
            content_name = content_list[index]
            # print(3)
        else:
            item_list.append(line)
            # print(4)
            continue

for key in output:
    for i in range(len(output[key])):
        element = output[key][i]
        tmp = element.split('-', 1)
        # print(tmp)
        # print(len(tmp))
        if len(tmp) == 1:
            output[key][i] = {"sub_content" : tmp[0]}
        else:
            output[key][i] = {"sub_content" : tmp[0], "description": tmp[1]}

with open("/Users/andrewwonwhoonah/Github-Tag-Embedder/sindresorhus/Machine_Learning/output.json", "w") as json_file:
    json.dump(output, json_file)