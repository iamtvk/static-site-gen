from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value = None, props=None) -> None:
        super().__init__(tag, value,None, props)


    def to_html(self) -> str:
        if self.value is None:
            raise ValueError("Value string is not given")
        if self.tag:
            return f'<{self.tag}{self.props_tohtml()}>{self.value}</{self.tag}>'
        return f'{self.value}'


