import json
# if you are using python 3, you should
import urllib.request
#import urllib2


# change the url according to your own corename and query
inurl = 'http://18.223.184.7:8983/solr/DFR/select?fl=id%2C%20score&q=text_en%3A%20%20Aleppo%20HQ&rows=20'
outfn = 'output10.txt'


# change query id and IRModel name accordingly
qid = ''
IRModel='DFR'
outf = open(outfn, 'a+')
#data = urllib2.urlopen(inurl)
# if you're using python 3, you should use
data = urllib.request.urlopen(inurl)

docs = json.load(data)['response']['docs']
# the ranking should start from 1 and increase
rank = 1
for doc in docs:
    outf.write("010" + ' ' + 'Q0' + ' ' + str(doc['id']) + ' ' + str(rank) + ' ' + str(doc['score']) + ' ' + IRModel + '\n')
    rank += 1
outf.close()
