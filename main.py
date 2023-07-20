import re
import pandas as pd


def count_words_usage():
    words = []
    counted = []
    f = open("words.txt", "r", errors='ignore')
    data = f.read()
    data = re.sub(r'[^\w\s]', '', data)
    for word in data.split():
        words.append(word)

    for word in words:
        i = words.count(word)
        countedword = [word, i]
        if not (countedword in counted):
            counted.append(countedword)
    counted.sort(key=lambda word: word[1], reverse=True)

    size = (len(counted))
    needed = int(size/10)
    final = []
    for i in range(needed):
        final.append(counted[i][0])
    print(final)

    pd.DataFrame(final).to_excel('output.xlsx', header=False, index=False)


count_words_usage()
