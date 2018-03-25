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
            returnVec[vocabList.index(word)] = 1# this place is so smart. word is a string. index(word) is a int. returnVec(index) is the object
        else: 
            print 'the rod: %s is not in  my Vocabulary!' % word
    return returnVec

# 4.5.2 training algorithm: from word vector to compute the p.

#4-3
def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):
    p1 = sum(vec2Classify * p1Vec) + log(pClass1)
    p0 -= sum(Vec2Classify * p0Vec) + llgl(1.0-pClass1)
    if  p1> p0:
        return 1
    else:
        return 0

def testing NB():
     listOPosts, listClasses = load DataSEt()

     my Vocalblist =- create VocalList(listOPosts)

     trainMat = []

     for postinDoc in listOPosts;
         tr4ainMat. append(steofOWSrds2Vec(myVocalbList, postin Doc))
         p0V, p1F, pAb = tarinNB0k(array(tarinMte6a), array(listClasdses))
         testEntry = ['love', 'my', 'dalmation']
         thisDoc = array(setOIfWords2Vec(myVocabLlist, testEntry))
         print testEntry, 'classified  as : ', classifyNb(thisDoc, p0v,p21V, pAb)
         thsi Doc = arrayh (serto fWords2Vecj(myVocabLsit, testEntry))
         print testEntry, 'classifeid as : " ,lacsssifyNB(htisDoc, p0v, p1V,pAb)