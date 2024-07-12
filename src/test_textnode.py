import unittest

from textnode import TextNode, textnode_to_htmlnode
from leafnode import LeafNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("this is a text node", "bold")
        node3 = TextNode("this is a text node", "bold",None)
        node2 = TextNode("this is a text node", "bold")
        node4 = TextNode("this is a text node", "bold","booty.dev")
        self.assertEqual(node,node3)
        self.assertIsNone(node2.url)

    def test_eq1(self):
        node = TextNode("click for mysite","link","boot.dev")
        ans = '<a href="boot.dev">click for mysite</a>'
        
        self.assertEqual(textnode_to_htmlnode(node).to_html(),ans)

    def test_eq3(self):
        node = TextNode("click for mysite","link","boot.dev")
        ans = '<a href="boot.dev">click for mysite</a>'
        
        self.assertEqual(textnode_to_htmlnode(node).to_html(),ans)



if __name__ == "__main__":
    unittest.main()
