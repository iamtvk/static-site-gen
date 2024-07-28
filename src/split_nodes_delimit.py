import re
from textnode import *


def split_nodes_delimiter(old_nodes,delimiter,text_type):
    _nodes = []
    returnTextNodeObjs = []
    for _node in old_nodes:
        if _node.text_type != "text":
            returnTextNodeObjs.append(_node)
            continue

        if _node.text_type == text_type_text:
            escaped_delimiter = re.escape(delimiter)
            pattern = re.compile(fr'({escaped_delimiter}.*?{escaped_delimiter})')

            _nodes += pattern.split(_node.text)
            if "" in _nodes :
                _nodes.remove("")

            for i in range(0,len(_nodes)):
                 returnTextNodeObjs.extend([TextNode(_nodes[i].replace(delimiter,""),"text" if delimiter not in _nodes[i] else text_type)])

    return returnTextNodeObjs
#

# def split_nodes_delimiter(old_nodes, delimiter, text_type):
#     new_nodes = []
#     for old_node in old_nodes:
#         if old_node.text_type != text_type_text:
#             new_nodes.append(old_node)
#             continue
#         split_nodes = []
#         sections = old_node.text.split(delimiter)
#         if len(sections) % 2 == 0:
#             raise ValueError("Invalid markdown, formatted section not closed")
#         for i in range(len(sections)):
#             if sections[i] == "":
#                 continue
#             if i % 2 == 0:
#                 split_nodes.append(TextNode(sections[i], text_type_text))
#             else:
#                 split_nodes.append(TextNode(sections[i], text_type))
#         new_nodes.extend(split_nodes)
#     return new_nodes
#
# print(split_nodes_delimiter([TextNode("this is the code example ```echo hello world``` ",text_type_text)],'```',text_type_code))


def extract_markdown_images(text) -> list[str] :
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)",text)
    return matches
def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)",text)
    return matches


def split_node_links(old_nodes):
    _nodes =[]
    returnTextNodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            _nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            _nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})",1)

            if len(sections) != 2:
                raise ValueError("Invalid Markdown, Link section not closed")

            if sections[0] != "":
                _nodes.append(TextNode(sections[0], text_type_text))
            _nodes.append(TextNode(link[0], text_type_link, link[1]))
            original_text = sections[1]

        if original_text != "":
            _nodes.append(TextNode(original_text, text_type_text))
    return _nodes

def split_node_images(old_nodes):
    _nodes =[]
    returnTextNodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            _nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_images(original_text)
        if len(links) == 0:
            _nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"![{link[0]}]({link[1]})",1)

            if len(sections) != 2:
                raise ValueError("Invalid Markdown, Link section not closed")

            if sections[0] != "":
                _nodes.append(TextNode(sections[0], text_type_text))
            _nodes.append(TextNode(link[0], text_type_image, link[1]))
            original_text = sections[1]

        if original_text != "":
            _nodes.append(TextNode(original_text, text_type_text))

    return _nodes



