import pickle
import gensim,pdb

words_set = pickle.load(open("word_set.pkl","r"))

model = gensim.models.KeyedVectors.load_word2vec_format('../GoogleNews-vectors-negative300.bin', binary=True)


model_part = {}
for word in words_set:
    if(word in model):
        model_part[word] = model[word]
#pdb.set_trace()

pickle.dump(model_part,open("word_embedding_dict.pkl","w"))