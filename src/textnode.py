from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE_TEXT = "code text"
    LINK = "link"
    IMAGES = "images"

class TextNode:
    def __init__(self, TEXT, TEXT_TYPE, URL):
        self.TEXT = TEXT,
        self.TEXT_TYPE = TEXT_TYPE,
        self.URL = URL,

    def __eg__(self, other):
        if self == other:
            return True
        return False
    
    def __repr__(self):
        return f"TextNode({self.TEXT}, {self.TEXT_TYPE}, {self.URL})"