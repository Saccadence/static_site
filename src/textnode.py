from enum import Enum

class TextType(Enum):
    PLAIN = "text"
    BOLD = "*text*"
    ITALIC = "_text_"
    CODE = "`text`"
    LINK = "[anchor](url)"
    IMAGE = "![alt](url)"

class TextNode():
    def __init__(self):
        self.text = TextType.PLAIN
        self.text_type = 