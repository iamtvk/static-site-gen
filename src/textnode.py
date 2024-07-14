from leafnode import LeafNode
from htmlnode import HTMLNode


text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

class TextNode:

    def __init__(self,text,text_type,url = None) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url


    def __eq__(self, other: object) -> bool:
        if not isinstance(other,TextNode):
            return False
        return other.text == self.text and other.text_type == self.text_type and other.url == self.url

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

def textnode_to_htmlnode(text_node : TextNode) -> LeafNode | None:
    if text_node.text_type not in [ "text", "bold", "italic", "code", "link", "image" ]:
        raise ValueError("Invalid Value for text_type")
    if text_node.text_type == "text":
        text_type_text = LeafNode(None,text_node.text,None)
        return text_type_text
    if text_node.text_type == "bold":
        text_type_bold = LeafNode("b",text_node.text,None)
        return  text_type_bold
    if text_node.text_type == "italic":
        text_type_italic = LeafNode("i",text_node.text,None)
        return text_type_italic

    if text_node.text_type == "code":
        text_type_code = LeafNode("code",text_node.text,None)
        return text_type_code

    if text_node.text_type == "link":
        text_type_link = LeafNode("a",text_node.text,{"href" : text_node.url})
        return text_type_link

    if text_node.text_type == "image":
        text_type_image = LeafNode("img","",{"src" : text_node.url, "alt" : text_node.text})
        return text_type_image

