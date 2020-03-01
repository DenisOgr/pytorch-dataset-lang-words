from glob import glob
import random
for file in glob('_*'):
    with open(file, encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
        max_idx = len(lines)
        words = []
        while len(words) < 2000:
            idx = random.randint(0, max_idx-1)
            word = lines[idx].rstrip().lower()
            if len(word) > 2 and not word in words:
                words.append(word)
        print("File: ", file, " lines: ", len(words))
        with open('results_2000/%s'%file, 'w') as fw:
            for word in words:
                fw.write(word+"\n")
