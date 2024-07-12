import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node1 = HTMLNode("p","this is a qwesome ",None,{"href": "boot.dev","target" : "blank"})
        node2 = HTMLNode("p","this is a qwesome ",node1,{"href": "www.boot.dev","target" : "_blank","nothing":"something"})

        self.assertEqual(node1.props_tohtml() ,' href="boot.dev" target="blank"')
        self.assertEqual(node2.children.props_tohtml() ,' href="boot.dev" target="blank"')
        self.assertEqual(node2.children.props,node1.props)


if __name__ == "__main__" :
    unittest.main()


