with open('./1_no_enter.txt', 'w') as dst:
    with open("/Users/andrewwonwhoonah/Github-Tag-Embedder/sindresorhus/Machine_Learning/0_raw.txt", 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            if len(line) != 1:
                dst.write(line)
