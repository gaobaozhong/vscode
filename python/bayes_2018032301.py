#coding:utf

def loadDataSet():#load a data set. it conclude a variable named postinglist. posting is a needed something. list ia a type including some string.
    postinglist = [
        ['my', 'dog','has','flea','problem','help','please'],#my dog has flea, this iss a problem ,please help me.
        ['maybe','not','take','him','to','dog','park','stupid'],#maybe do not take him to find dog in park ,this is stupid
        ['my','dalmation','is','so','cute','I',';love','him'],# my dalmation is so cute, i love him
        ['stop','posting','stupid','worthless','garbage'],# Stop posting , this is stupid, it is worthless and you are garbage
        ['mr','lickes','ate','my','steak','how','to','stop','him'],#mr lickes, ate my steak, how to stop him
        ['quit','buying','worthless','do','food','stupid']#quit buying , it is worthless to do the stupid thing. food.
    ]
    classVec = [0,1,0,1,0,1]# According to the postinglist ,this is the class Vectory 

    return postinglist,classVec

def createVocabList(dataSet):# create the vocability list. The data Set will be splited to teh vocability.
    vocabSet = set([])# define the vocab set as a null list
    for document in dataSet:#for any document in dataset
        vocabSet = vocabSet | set(document)# let vocabset include document or others.
    return list(vocabSet) #??

def setOfWords2Vec(vocabList,inputSet):
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else: 
            print 'the rod: %s is not in  my Vocabulary!' % word
    return returnVec
