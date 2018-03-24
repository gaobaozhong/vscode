import bayes_2018032301 as bayes

listOPosts, listClasses = bayes.loadDataSet()
myVocabList = bayes.createVocabList(listOPosts)
print myVocabList

bayes.setOfWords2Vec(myVocabList,listOPosts[0])