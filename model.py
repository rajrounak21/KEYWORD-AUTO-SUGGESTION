import numpy as np
import pandas as pd
from collections import Counter
import textdistance
import re


words = []
with open("C:\\Users\\rouna\\Downloads\\autocorrect book.txt",'r',encoding='utf-8') as f:
    data = f.read()
    data = data.lower()
    word = re.findall('\w+',data)
    words +=word
print(words)

V= set(words)
word_freq_dict = Counter(words)

Total_words_freq = sum(word_freq_dict.values())
probs ={}
for k in word_freq_dict.keys():
    probs[k] = word_freq_dict[k] / Total_words_freq

# create a function for auto  correction
def autocorrect(word):
    word = word.lower()
    if word in probs:
        print(f"The word '{word}' is already correct.")
        return word

    similarities = [textdistance.jaccard.normalized_similarity(w, word) for w in word_freq_dict.keys()]
    df = pd.DataFrame({
        'word': list(word_freq_dict.keys()),
        'prob': [probs[w] for w in word_freq_dict.keys()],
        'similarity': similarities
    })

    output = df.sort_values(['similarity', 'prob'], ascending=[False, False]).head(10)
    return output


# Example usage:
result = autocorrect('machin')
print(result)
