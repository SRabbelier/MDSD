from xml.etree import ElementTree
from xml.dom import minidom

main_const = '__main__'

def copyStream(stream):
    return ElementTree.fromstring(ElementTree.tostring(stream))

def ident(i):
    return i

def streamFromString(string):
    return ElementTree.fromstring(string)

def streamToString(stream):
    as_string = ElementTree.tostring(stream)
    as_dom = minidom.parseString(as_string)
    as_xml = as_dom.toprettyxml()
    return as_xml

def streamSize(*streams):
    return [len(i.findall("channel/item")) for i in streams]

def isEmpty(stream):
    return not streamSize(stream)[0]
