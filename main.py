import re
import pandas as pd

def CountWordsUsage():
    Words = []
    Counted = []
    f = open("words.txt", "r", errors='ignore')
    data = f.read()
    data = re.sub(r'[^\w\s]', '', data)
    for words in data.split():
        Words.append(words)

    for word in Words:
        i = Words.count(word)
        countedWord = [word, i]
        while(word in Words):
            Words.remove(word)
        if ((countedWord in Counted)==False):
            Counted.append(countedWord)
    Counted.sort(key=lambda word: word[1], reverse=True)

    Size = (len(Counted))
    Needed = int(Size/10)
    Final = []
    for i in range(Needed):
        Final.append(Counted[i][0])
    print(Final)

    pd.DataFrame(Final).to_excel('output.xlsx', header=False, index=False)

CountWordsUsage()