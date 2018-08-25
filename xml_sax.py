import requests
import xml.sax


class MyContentHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.slideCount = 0
        self.itemCount = 0
        self.isInTitle = False

    # Handle startElement
    def startElement(self, tagName, attrs):
        if tagName == "slideshow":
            print("Slideshow title: " + attrs["title"])
        elif tagName == "slide":
            self.slideCount += 1
        elif tagName == "item":
            self.itemCount += 1
        elif tagName == "title":
            self.isInTitle = True

    # Handle endElement
    def endElement(self, tagName):
        if tagName == "title":
            self.isInTitle = False

    # Handle text data
    def characters(self, chars):
        if self.isInTitle:
            print("Title: " + chars)

    # Handle startDocument
    def startDocument(self):
        print("About to Start")

    # Handle endDocument
    def endDocument(self):
        print("Finishing up!")


# main function
handler = MyContentHandler()
url = "http://httpbin.org/xml"
response = requests.get(url)
# print(response.text)

# Call the parseString method on the XML text content recieved
xml.sax.parseString(response.text, handler)

# print slide and item count
print("slides count {}".format(handler.slideCount))
print("slides item count {}".format(handler.itemCount))



