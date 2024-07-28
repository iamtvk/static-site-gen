class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props


    def to_html(self):
        raise NotImplementedError

    def props_tohtml(self) -> str:
        if not self.props:
            return ""
        htmlprops = ""
        for prop in self.props:
            htmlprops += f' {prop}="{self.props[prop]}"'
        return htmlprops

