import htmlnode
import parentnode
from split_nodes_delimit import *
from parentnode import *
from htmlnode import *
from textnode import *

def text_to_textnodes(text):
    """converts text to text nodes"""
    nodes = [TextNode(text,text_type_text)]
    nodes = split_nodes_delimiter(nodes,"**",text_type_bold)
    nodes = split_nodes_delimiter(nodes,"*",text_type_italic)
    nodes = split_nodes_delimiter(nodes,'```',text_type_code)
    nodes = split_nodes_delimiter(nodes,"`",text_type_code)
    nodes = split_node_images(nodes)
    nodes = split_node_links(nodes)
    ret = []
    [ret.append(x) for x in nodes if x not in ret]
    return ret

def markdown_to_block(mdDoc: str):
    """divindes given markdown Doc to Blocks
        Args:
        mdDoc(str) : markdown document
        Returns:
        List[str] """
    blocks = re.split(r'\n\s*\n',mdDoc)
    blocks = [block.strip() for block in blocks]
    return blocks



def block_to_block_type(block):
    """
    args : markdown block
    return : type of markdown block
    """

    if block[0:6] == '######':
        block_type = "h6"
    elif block[0:5] == '#####':
        block_type = "h5"
    elif block[0:4] == '####':
        block_type = "h4"
    elif block[0:3] == '###':
        block_type = "h3"
    elif block[0:2] == '##':
        block_type = "h2"
    elif block[0:1] == '#':
        block_type = "h1"

    elif block[0:3] == '```':
        block_type = "code"

    elif block[0] == '>':
        block_type = "blockquote"

    elif block[0] == '*' or block[0] == '-':
        block_type = "ul"

    elif block[0].isdigit() :
        block_type = "ol"

    else:
        block_type = "p"

    return block_type



    
def add_list_items(html_string):
    """ adds <li> tags to list items for both ul and ol"""
    def add_li_tags(match):
        # Extract the content between the list tags
        list_content = match.group(2).strip()
        # Split the content by newline and wrap each item with <li> tags
        items = [f"<li>{item.strip()}</li>" for item in list_content.split('\n') if item.strip()]
        # Join the list items and return the updated list string
        return f"{match.group(1)}\n" + "\n".join(items) + f"\n{match.group(3)}"
    
    # Use regex to match <ul> or <ol> tags and their content
    updated_string = re.sub(r'(<ul>|<ol>)([\s\S]*?)(</ul>|</ol>)', add_li_tags, html_string)
    return updated_string



def text_to_children(block):
    """takes in block of md and returns the respective text nodes conveerted to html nodes"""
    textnodes = text_to_textnodes(block)
    childs = []
    for node in textnodes:
        childs.append(textnode_to_htmlnode(node))
    return childs



def md_to_html_node(md_text):
    md_blocks = markdown_to_block(md_text)
    text_nodes = []
    html_nodes = []

    for block in md_blocks:
         # text_nodes.append((text_to_textnodes(block) + ([block_to_block_type(block)])))
        if block_to_block_type(block) in ("h1","h2","h3","h4","h5","h6",):
            texty = ParentNode(tag=f"{block_to_block_type(block)}",children= text_to_children(block), props=None).to_html()
            texty = texty.replace('#',"")
            html_nodes.append(add_list_items(texty))
            continue

        if block_to_block_type(block) == "code":
            html_nodes.append(ParentNode(tag=f"pre",children= text_to_children(block), props=None).to_html())
            continue

        if block_to_block_type(block) == "ol":
            texty = ParentNode(tag=f"{block_to_block_type(block)}",children= text_to_children(block), props=None).to_html()
            html_nodes.append(re.sub(r'\b\d+\.\s*','',add_list_items(texty)))
            continue

        if block_to_block_type(block) == "ul":
            texty = ParentNode(tag=f"{block_to_block_type(block)}",children= text_to_children(block), props=None).to_html()
            html_nodes.append((add_list_items(texty)).replace('-',''))
            continue

        if block_to_block_type(block) == "blockquote":
            block = block.replace('>','')
            texty = ParentNode(tag="blockquote",children= text_to_children(block), props=None).to_html()
            html_nodes.append(texty)
            continue


        html_nodes.append(ParentNode(tag=f"{block_to_block_type(block)}",
                                     children= text_to_children(block), props=None).to_html())

    # for textnode in text_nodes:
        # html_nodes.append((textnode_to_htmlnode(textnode[0])).to_html())

    return f'<div>{"".join(html_nodes)}</div>'



