#####-------------GLOVE------------
import codecs
import numpy as np
import pandas as pd

def load_glove_model(gloveFile):
    #print "Loading Glove Model"
    f = codecs.open(gloveFile,'r', encoding='utf-8')
    model = {}
    for line in f:
        splitLine = line.split()
        word = splitLine[0]
        embedding = np.array([float(val) for val in splitLine[1:]])
        model[word] = embedding
    #print "Done.",len(model)," words loaded!"
    return model

#------Load the model
glove = load_glove_model('/Users/pemagurung/Downloads/glove.6B/glove.6B.50d.txt')
#------transform simple text to vectors
text = "hello!! my name is Pema"
vectors= glove.get(text, np.zeros(50))
print vectors