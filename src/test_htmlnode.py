import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("test", "test", ["test", "test2"], {"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode("test")
        self.assertNotEqual(node, node2)
    
    def test_repr(self):
        node = HTMLNode("test", "test", ["test", "test2"], {"href": "https://www.google.com", "target": "_blank"})
        node_text = "HTMLNode(test, test, ['test', 'test2'], {'href': 'https://www.google.com', 'target': '_blank'})"
        self.assertEqual(repr(node), node_text)
    
    def test_props(self):
        node = HTMLNode(None, None, None, {"href": "https://www.google.com", "target": "_blank"})
        node_text = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), node_text)
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

if __name__ == "__main__":
    unittest.main()