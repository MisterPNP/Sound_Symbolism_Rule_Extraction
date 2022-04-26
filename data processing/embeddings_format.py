import json

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

inputword_list = ['test']

currstr = ''
indextracker = []

for word in inputword_list:
    currstr, syncount = generateSynonyms(currstr, word)
    #print(syncount)
    indextracker.append(syncount)

#remove last space, then surround in single quotes
currstr = currstr[:-1]
currstr = f"'{currstr}'"

sf = open("ipa_embeddings.txt", "a")
sf.write(currstr)
sf.close()

print(indextracker)