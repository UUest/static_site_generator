class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, HTMLNode):
            return False
        return (
            self.tag == other.tag and
            self.value == other.value and
            self.children == other.children and
            self.props == other.props
        )
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self) -> str:
        return "".join(map(lambda item: f' {item[0]}="{item[1]}"', self.props.items()))
    
    def __repr__(self) -> str:
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"

   
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