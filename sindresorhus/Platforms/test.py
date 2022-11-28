str1 = "Node.js - Async non-blocking event-driven JavaScript runtime built on Chrome's V8 JavaScript engine.\n"
str2 ="Frontend Development\n"
output = {"platforms": [str1, str2]}

for key in output:
    for i in range(len(output[key])):
        element = output[key][i]
        tmp = element.split('-', 1)
        print(tmp)
        print(len(tmp))
        if len(tmp) == 1:
            output[key][i] = {"sub_content" : tmp[0]}
        else:
            output[key][i] = {"sub_content" : tmp[0], "description": tmp[1]}

print(output)