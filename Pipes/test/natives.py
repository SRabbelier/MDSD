import urllib2
from pipes_builtins import copyStream
from pipes_builtins import streamFromString

def func_join(stream_first, stream_second):
    result = copyStream(stream_first)
    channel = result.find("channel")
    for item in stream_second.findall("channel/item"):
        channel.append(item)
    return result

def func_split(stream_stream, arg_from=None):
    before = copyStream(stream_stream)
    after = copyStream(stream_stream)
    arg_from -= 1
    
    channel = before.find("channel")
    items = before.findall("channel/item")
    for item in items[arg_from:]:
        channel.remove(item)

    channel = after.find("channel")
    items = after.findall("channel/item")
    for item in items[:arg_from]:
        channel.remove(item)

    return before, after

def func_feed(arg_url=None):
    feed = urllib2.urlopen(arg_url).read()
    return streamFromString(feed)

