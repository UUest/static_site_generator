from htmlnode import HTMLNode
 
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)
        
    def __eq__(self, other: object) -> bool:
        return super().__eq__(other)
    
    def to_html(self) -> str:
        if self.tag is None or self.tag == '':
            raise ValueError("ParentNode must have a tag")
        elif self.children is None or self.children == []:
            raise ValueError("ParentNode must have children")
        children_string = "".join(list(map(lambda node: node.to_html(), self.children)))
        return f"<{self.tag}>{children_string}</{self.tag}>"