filename="input_file"
with open(filename,"r") as f:
    for line in f.readlines():
        words = len(line.strip())
        line=line.strip()
        print(line,words)