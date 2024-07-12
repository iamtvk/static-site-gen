from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self, tag=None, children = None, props=None) -> None:
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag is not given")
        if self.children is None:
            raise ValueError("Children is not defined")
        __childs = ""
        for node in self.children :
            __childs += node.to_html()
        return f'<{self.tag}{self.props_tohtml()}>{__childs}</{self.tag}>'
