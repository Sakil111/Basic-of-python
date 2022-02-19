import xml.etree.ElementTree as ET
data='''<?xml version="1.0" encoding="UTF-8"?>
<metadata>
<food>
    <item name="breakfast">Idly</item>
    <price>$2.5</price>
    <description>
   Two idly's with chutney
   </description>
    <calories>553</calories>
</food>
</metadata>
'''
myroot=ET.fromstring(data)
print(myroot[0].tag)
# want to retrieve all first-child tags of the root(All the items returned are the child attributes and tags of food)
for x in myroot[0]:
    print(x.tag,x.attrib)
# To separate out the text from XML
for x in myroot[0]:
    print(x.text)
data1="""<feed xml:lang='en'>
    <title>HackerRank</title>
    <subtitle lang='en'>Programming challenges</subtitle>
    <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
    <updated>2013-12-25T12:00:00</updated>
</feed>"""
myroot1=ET.fromstring(data1)
var=0
for x in myroot1.iter():
    var+=len(x.attrib)
print(var)