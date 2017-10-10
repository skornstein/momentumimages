import re
import urllib

url = "https://d3cbihxaqsuq0s.cloudfront.net/"
#Alt URL:
#https://s3.amazonaws.com/123rf-chrome/

text = urllib.urlopen(url).read()
table = re.findall(r'<Key>(.+?)<\/Key>', text)
counter = 1

#assumes first image key is invalid
for i in xrange(1,len(table)):
    suffix = (table[i])
    #print suffix
    name = suffix[-(len(suffix)-suffix.find('/')-1):]
    #print name
    image = urllib.urlretrieve(url+suffix,"C:\Users\\skorn\\Pictures\Momentum Images\\"+name)
    print "%d images downloaded - %d remaining" % (counter, len(table)-counter-1)
    counter += 1