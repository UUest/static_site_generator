class TextNode:
    def __init__(self, text: str, text_type: str, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
        
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, TextNode):
            return False
        return (
            self.text == other.text and
            self.text_type == other.text_type and
            self.url == other.url
        )
        
    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    

def main():
    TestNode = TextNode("this is a TextNode", "italic", "www.google.com")
    print(TestNode)