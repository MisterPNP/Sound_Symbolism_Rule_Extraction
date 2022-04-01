import pandas as pd
import numpy as np

df = pd.read_csv('synonyms.csv')

#cast our synonyms to strings, split synonyms
df['synonyms'] = df['synonyms'].astype(str)
df['synonyms'] = df['synonyms'].str.replace('|', ';')
df['synonyms'] = df['synonyms'].str.split(';')
#print(df.tail(10)) 

#print(df['part_of_speech'].unique())

def cluster_synonyms(allwords, iteration):

    startlen = len(allwords)
    nl = set(allwords)

    for word in allwords:
        synonyms = df.loc[df['lemma'] == word]['synonyms'].to_numpy()
        dumpIntoSet(nl, synonyms)
    
    #turn back to list to pass as param
    new_words = list(nl)
    endlen = len(new_words)

    if(startlen == endlen): #if we didn't add more words, we converge
        return new_words

    if(iteration == 1):
        return new_words

    print(iteration)
    print(new_words)

    return cluster_synonyms(new_words, iteration+1)


def dumpIntoSet(word_set, new_words):
    for word in new_words:
        word_set.update(word)

init = np.array(['glow'])
syns = cluster_synonyms(init, 0)
print(syns)

'''

iteration 1: 45%
iteration 2: 20%
iteration 3: 2%

'''

#synonyms.extend(allwords)
#print(type(allwords))
#print(type(synonyms))