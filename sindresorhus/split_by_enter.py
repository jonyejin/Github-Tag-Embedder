with open('./main_0.txt', 'w') as dst:
    with open("/Users/andrewwonwhoonah/Github-Tag-Embedder/sindresorhus/main_raw.txt", 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            if len(line) != 1:
                dst.write(line)
