from __future__ import division
from sklearn.cluster import MiniBatchKMeans
from numbers import Number
from pandas import DataFrame
import sys, codecs, numpy, json


class ListWords(dict):
    def __missing__(self, key):
        value = self[key] = []
        return value

    def __add__(self, x):
        if not self and isinstance(x, Number):
            return x
        raise ValueError

    def __sub__(self, x):
        if not self and isinstance(x, Number):
            return -1 * x
        raise ValueError


def build_word_vector_matrix(vector_file, n_words):
    numpy_arrays = []
    labels_array = []
    with codecs.open(vector_file, 'r', 'latin1') as f:
        for c, r in enumerate(f):
            sr = r.lower().split()

            if len(sr) != 301:
                continue

            try:
                labels_array.append(sr[0])
                numpy_arrays.append(numpy.array([float(i) for i in sr[1:]]))

            except ValueError:
                print
                c, len(sr)

            if c == n_words:
                return numpy.array(numpy_arrays), labels_array

    return numpy.array(numpy_arrays), labels_array


def find_word_clusters(labels_array, cluster_labels):
    cluster_to_words = ListWords()
    for c, i in enumerate(cluster_labels):
        cluster_to_words[str(i)].append(labels_array[c])
    return cluster_to_words


if __name__ == "__main__":
    input_vector_file = sys.argv[1]
    n_words = int(sys.argv[2])
    reduction_factor = float(sys.argv[3])
    clusters_to_make = int(n_words * reduction_factor)
    df, labels_array = build_word_vector_matrix(input_vector_file, n_words)
    kmeans_model = MiniBatchKMeans(init='k-means++', n_clusters=clusters_to_make)
    kmeans_model.fit(df)

    cluster_labels = kmeans_model.labels_
    cluster_inertia = kmeans_model.inertia_
    cluster_to_words = find_word_clusters(labels_array, cluster_labels)

    with open("glove_clusters_" + str(sys.argv[2]) + "_words.json", 'w') as json_out:
        json.dump(cluster_to_words, json_out)