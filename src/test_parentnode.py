import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_eq(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        nodeHtml = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"

        self.assertEqual(node.to_html(),nodeHtml)

    def test_eq_false(self):
        node2 = ParentNode(
            "div",
            [
                LeafNode("b", "Bold text",{"size":69,"color":"red"}),
                LeafNode(None, "Normal text",{"size":69,"color":"red"}),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text",{"size":69,"color":"blue"}),
            ],
        )

        nodeHtml = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"

        self.assertNotEqual(node2.to_html(), nodeHtml)

    def test_eq_false2(self):
        node2 = ParentNode(
            "div",
            [
                LeafNode("b", "Bold text",{"size":69,"color":"red"}),
                LeafNode(None, "Normal text",{"size":69,"color":"red"}),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text",{"size":69,"color":"blue"}),
            ],
        )

        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
                node2,
            ],
        )

        nodeHtml = f'<p><b>Bold text</b>Normal text<i>italic text</i>Normal text{node2.to_html()}</p>'

        self.assertEqual(node.to_html(), nodeHtml)


if __name__ == "__main__":
    unittest.main()
