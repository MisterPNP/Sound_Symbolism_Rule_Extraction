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
'''
def hamming_distance(string1, string2):
	dist_counter = 0
    shorter = min(len(string1), len(string2))
	for n in range(shorter):
		if string1[n] != string2[n]:
			dist_counter += 1
	return dist_counter
'''

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

if(len(sys.argv) < 2):
    print("Please give a word as cmd line argument")
    exit(0)

inputword = sys.argv[1]#'abominable'

df = pd.read_csv('../Data/synonyms/synonyms.csv')

# cast our synonyms to strings, split synonyms
df['synonyms'] = df['synonyms'].astype(str)
df['synonyms'] = df['synonyms'].str.replace('|', ';')
df['synonyms'] = df['synonyms'].str.split(';')

init = np.array([inputword])
syns = cluster_synonyms(init, 0)
#print(len(syns))

#first, make our list of IPA representations
file = open('../Data/IPA Data/en_US.txt', 'r', encoding='utf8')
data = format_file(file)

#print(data)
data_table = {}
for entry in data:
    data_table[entry[0]] = entry[1]

syns_ipa = []

outstr = ''
for word in syns:
    try:
        ipa = data_table[word]
        syns_ipa.append(ipa)
        #print(word)
        #print(ipa)
        outstr += '"{}" '.format(ipa)
    except:
        test=0
        #print('word not found in dictionary: {}'.format(word))

#remove last space, then surround in single quotes
outstr = outstr[:-1]
outstr = f"'{outstr}'"
print(syns)
print(syns_ipa)
'''
for i in range(0, len(syns_ipa)):
    for j in range(i, len(syns_ipa)):
        hd = hamming_distance(syns_ipa[i], syns_ipa[j])
        print(hd)
'''
#print(syns)
file.close()


'''
compute size of strings (len of all words in string)
'''

'''
Theory

We can say that a phoenetic sound is symbollic
if it appears abnormally often for a set of words that
are semantically similar, than it does for semantically 
disimlar words

E.g.) If the sound 'ɡɫ' appears in 1% of all words
but appears in 70% of words that are semantically similar
to the word 'glow', we can assume a strong influence of sound
symbolism

'''