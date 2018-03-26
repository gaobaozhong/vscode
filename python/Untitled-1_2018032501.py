import bayes_2018032301 as bayes
import feedparser
ny = feedparser.parse('http://newyork.craigslist.org/res/index.rss')
sf = feedparser.parse('http://sfbay.craigslist.org/apa/index.rss')
vocabList,pSF,pNY = bayes.localWords(ny,sf)
bayes.getTopWords(ny,sf)
print ny['entries'][0]['summary']
print sf['entries'][0]['summary']
