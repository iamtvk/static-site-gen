import re
from textnode import *

node = TextNode("this is a text with a `code block` word",text_type_text)

def split_nodes_delimiter(old_nodes,delimiter,text_type):
    _nodes = []
    returnTextNodeObjs = []
    for _node in old_nodes:
        if _node.text_type != "text":
            returnTextNodeObjs.append(_node)

        if _node.text_type == text_type_text:
            escaped_delimiter = re.escape(delimiter)
            pattern = re.compile(fr'({escaped_delimiter}.*?{escaped_delimiter})')

            _nodes += pattern.split(_node.text)
            if "" in _nodes :
                _nodes.remove("")
            for i in range(0,len(_nodes)):
                 returnTextNodeObjs.extend([TextNode(_nodes[i].replace(delimiter,""),"text" if delimiter not in _nodes[i] else text_type)])

    return returnTextNodeObjs


def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)",text)
    return matches
def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)",text)
    return matches
