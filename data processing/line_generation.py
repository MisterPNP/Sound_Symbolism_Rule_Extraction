import pandas as pd
import numpy as np

def process_line(line):
    translation_table = dict.fromkeys(map(ord, '/ '), None)
    line = line.split()
    line = tuple((line[0], line[1].translate(translation_table)))
    return line

def format_file(input_file):
    data = []
    lines = input_file.readlines()
    for line in lines:
        if line[0] != "\'":
            tuple_line = process_line(line)
            data.append(tuple_line)

    return data


def cluster_synonyms(allwords, iteration):
    startlen = len(allwords)
    nl = set(allwords)

    for word in allwords:
        synonyms = df.loc[df['lemma'] == word]['synonyms'].to_numpy()
        dumpIntoSet(nl, synonyms)

    # turn back to list to pass as param
    new_words = list(nl)
    endlen = len(new_words)

    if (startlen == endlen):  # if we didn't add more words, we converge
        return new_words

    if (iteration == 0):
        return new_words

    return cluster_synonyms(new_words, iteration + 1)


def dumpIntoSet(word_set, new_words):
    for word in new_words:
        word_set.update(word)



#grab our list of synonyms

inputword = 'glow'

df = pd.read_csv('../Data/synonyms/synonyms.csv')

# cast our synonyms to strings, split synonyms
df['synonyms'] = df['synonyms'].astype(str)
df['synonyms'] = df['synonyms'].str.replace('|', ';')
df['synonyms'] = df['synonyms'].str.split(';')

init = np.array([inputword])
syns = cluster_synonyms(init, 0)
print(syns)

#first, make our list of IPA representations
file = open('../Data/IPA Data/en_US.txt', 'r', encoding='utf8')
data = format_file(file)

data_table = {}
for entry in data:
    data_table[entry[0]] = entry[1]

str = ''
for word in syns:
    try:
        ipa = data_table[word]
        str += """ "{}" """.format(ipa)
    except:
        print('word not found in dictionary: {}'.format(word))

print(str)

file.close()