import pickle
import os

dirname = (os.path.dirname(os.path.realpath(__file__)))

def loadData(name, isLabel):
    data = []
    handle = None
    if isLabel:
        handle = open(dirname +'/../dataset/' +name +'/labels.pickle', 'rb');
    else:
        handle = open(dirname +'/../dataset/' +name +'/dataset.pickle', 'rb');
    data = pickle.load(handle)
    handle.close()
    return data;

    