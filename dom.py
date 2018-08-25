import requests
import xml.dom.minidom


url = "http://httpbin.org/xml"
response = requests.get(url)
domtree = xml.dom.minidom.parseString(response.text)

rootnode = domtree.documentElement

#get the name of the root node and titles
print("The root element is {}".format(rootnode))
print("Title: {0}".format(rootnode.getAttribute("title")))

items = domtree.getElementsByTagName("item")
print("There are {0} item tags".format(items.length))

#data manipulation
#create a new item tag
newItem = domtree.createElement("item")

#add some text to the item
newItem.appendChild(domtree.createTextNode("This is some text from gbenga"))

#add the item to the first slide
firstSlide = domtree.getElementsByTagName("slide")[0]
firstSlide.appendChild(newItem)

#count again
items = domtree.getElementsByTagName("item")
print("There are {0} item tags".format(items.length))

from lxml import etree
url = "http://httpbin.org/xml"
result = requests.get(url)

doc = etree.fromstring(result.content)
#access attribute
print(doc.tag)
print(doc.attrb['title'])

#iterage over tags
for elem in doc.findall("slide"):
    print(elem.tag)

#create a new slide
newSlide = etree.Element(doc, "slide")
newSlide.text = "This is a new slide"

#count elements
slideCount = len(doc.findall("slide"))
itemCount = len(doc.findall(".//item"))


print("There are {0} slide tags".format(slideCount))

print("There are {0} item tags".format(itemCount))