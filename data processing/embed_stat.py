import json
import csv
import subprocess
from gruut_ipa import Pronunciation

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

def getEmbeddingsWordList():
    wordlist = []
    cluster_index = 0
    for c_id, cluster in embeddings.items():
        cluster_index += 1
        print('{} / {}'.format(cluster_index, len(embeddings.items())))
        if(len(cluster) < 3):
            continue
        for word in cluster:
            if word not in data_table:
                #print('word {} not found'.format(word))
                continue
            d = {
                'word': word,
                'ipa': seperatePhonemes(data_table[word]),
                'index': len(wordlist),
                'clusterID': c_id
            }
            wordlist.append(d)
    return wordlist

def seperatePhonemes(word):
    
    syl_list = Pronunciation.from_string(word).phones
    phonemes = ' '.join([x.text for x in syl_list])
    return phonemes
    #phonemes = subprocess.run(["python3", "-m", "gruut_ipa", "phonemes", "en-us", word], stdout=subprocess.PIPE).stdout.decode('utf-8')



def generateSynonyms(currstr, word):
    syns = getEmbeddedCluster(word)
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

def getEmbeddedCluster(word):
    for c_id, cluster in embeddings.items():
        if(word in cluster):
            return cluster
    return []

#read json data
f = open('../Data/Clusters/glove_clusters_10000_words.json', "r")
jsonstr = f.read()
embeddings = json.loads(jsonstr)

#read IPAs
file = open('../Data/IPA Data/en_US.txt', 'r', encoding='utf8')
data = format_file(file)

data_table = {}
for entry in data:
    data_table[entry[0]] = entry[1]

print(embeddings)

#load in adjectives
#with open('../Data/adjectives.txt') as file:
#    lines = file.readlines()
'''
#inputword_list = [x[:-1] for x in lines]
inputword_list = ['better', 'best', 'blue', 'broken', 'clear', 'giving', 'good', 'grand', 'heavy', 'light', 'ragged', 'sick']

currstr = ''
indextracker = []

for word in inputword_list:
    #print('{} / {}'.format(len(indextracker), len(inputword_list)))
    currstr, syncount = generateSynonyms(currstr, word)
    #print(syncount)
    indextracker.append(syncount)

#remove last space, then surround in single quotes
currstr = currstr[:-1]
currstr = f"'{currstr}'"

sf = open("ipa_embeddings.txt", "a")
sf.write(currstr)
sf.close()

#print(indextracker)
'''

'''

~4000 words for Pierre's RNN
if has less than 3 words in cluster, ignore
clusterID = json id

index, word, ipa, clusterID
1151, attached, a t t a c h e d, 12

'''