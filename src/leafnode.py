from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)
        
    def __eq__(self, other: object) -> bool:
        return super().__eq__(other)
        
    def to_html(self) -> str:
        if self.value is None or self.value == '':
            raise ValueError("All leaf nodes must have a value")
        elif self.tag is None or self.tag == '':
            return self.value
        elif self.props is None or self.props == {}:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self) -> str:
        return f"LeafNode(tag={self.tag}, value={self.value}, props={self.props})"