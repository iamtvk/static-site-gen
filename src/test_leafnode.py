from leafnode import LeafNode
import unittest


class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node1 = LeafNode("p", "This is a paragraph of text.")
        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})

        # <p>This is a paragraph of text.</p>
        # <a href="https://www.google.com">Click me!</a>
        self.assertEqual(node1.to_html(),"<p>This is a paragraph of text.</p>")
        self.assertEqual(node2.to_html(),'<a href="https://www.google.com">Click me!</a>')

        # soup1 = BeautifulSoup(node1.to_html(),'html.parser')
        # soup2 = BeautifulSoup("<p>This is a paragraph of text.</p>",'html.parser')
        # self.assertEqual(soup1,soup2)
