import pandas as pd
import numpy as np
import sys

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

def moreThanNSynonyms(allwords, n):
    new_words = []

    for word in allwords:
        init = np.array([word])
        syns = cluster_synonyms(init, 0)
        if(len(syns) > n):
            new_words.append(word)
    return new_words

def generateSynonyms(currstr, word):
    init = np.array([word])
    syns = cluster_synonyms(init, 0)
    countedsyns = 0
    for word in syns:
        try:
            ipa = data_table[word]
            if(ipa.endswith(',')):
                ipa = ipa[:-1]
            currstr += '"{}" '.format(ipa)
            countedsyns += 1
        except:
            test=0
    #return first the updated string, second the number of synonyms for this word
    return currstr, countedsyns

#grab our list of synonyms

inputword = 'better'
#inputword_list = []

df = pd.read_csv('../Data/synonyms/synonyms.csv')

# cast our synonyms to strings, split synonyms
df['synonyms'] = df['synonyms'].astype(str)
df['synonyms'] = df['synonyms'].str.replace('|', ';')
df['synonyms'] = df['synonyms'].str.split(';')

#print(len(syns))

#first, make our list of IPA representations
file = open('../Data/IPA Data/en_US.txt', 'r', encoding='utf8')
data = format_file(file)

#for using adjectives
with open('../Data/adjectives.txt') as file:
    lines = file.readlines()

data_table = {}
for entry in data:
    data_table[entry[0]] = entry[1]

#allwords = list(data_table.keys())
#inputword_list = moreThanNSynonyms(allwords, 20)
inputword_list = [x[:-1] for x in lines]

print(len(inputword_list))

#print(inputword_list)
#keep track of number of synonyms per word
indextracker = []

#iterate over our list of words
currstr = ''
for word in inputword_list:
    currstr, syncount = generateSynonyms(currstr, word)
    #print(syncount)
    indextracker.append(syncount)

#remove last space, then surround in single quotes
currstr = currstr[:-1]
currstr = f"'{currstr}'"
print(currstr)
print(indextracker)
print(inputword_list)

sf = open("ipa_synonyms.txt", "a")
sf.write(currstr)
sf.close()


file.close()


'''
compute size of strings (len of all words in string)
'''