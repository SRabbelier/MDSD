import urllib2
import feedparser
from xml.etree import ElementTree

def ident(i):
    return i

# untill a more useful decoration comes up
selector = ident

def create_element(scoped_name, content):
	head, rest = scope_name.split('/', 1)

	# base case
	if not rest:
    		e = Element(head, {}, text=content)
		return e

	# TODO: handle non-text content
  	e = Element(head, {}, {})
  	e.append(create_element(rest, content))
  	return e

def apply_loop(stream, on=None, assign=None, trans=lambda i: i, iterate='channel/item'):
	if not assign:
        	assign = on

	for item in stream.findall(iterate):
        	onelement = item.find(assign)
        	new_content = trans(onelement.text)
        	if assign == on:
            		item.text = new_content;
        	else:
            		new_element = create_element(assign, new_content)
            		item.append(new_element)
	return stream

def apply_filter(stream, on=None, query=None, rule="contains", match="all", filter="block"):
	should_filter = filter == "permit" # "permit" or "block"
	channel = stream.find("channel")
	found = False
	for item in stream.findall("channel/item"):
		if rule == "contains":
			if item.find(on).text.find(query) >= 0:
				found = True
		else:
			raise NotImplementedError("Rule '" + rule + "' is not valid")
		if found != should_filter:
			channel.remove(item)
	return stream

def extract_feed(url=None):
    feed = urllib2.urlopen(url).read()
    return ElementTree.fromstring(feed)

