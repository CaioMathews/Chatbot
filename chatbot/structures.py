from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime

@dataclass
class Intent:
    tag: str
    patterns: List[str]
    responses: List[str]


@dataclass
class Message:
    sender: str  
    content: str
    timestamp: datetime


@dataclass
class ChatHistory:

    messages: List[Message]

    def add_message(self, sender: str, content: str):
        msg = Message(sender=sender, content=content, timestamp=datetime.now())
        self.messages.append(msg)

    def last_message(self) -> Optional[Message]:
        
        if self.messages:
            return self.messages[-1]
        else:
            return None


@dataclass
class Node:
    key: int
    value: str
    left: Optional["Node"] = None
    right: Optional["Node"] = None


def insert(root: Optional[Node], key: int, value: str) -> Node:
    
    if root is None:
        return Node(key, value)

    if key < root.key:
        root.left = insert(root.left, key, value)

    elif key > root.key:
        root.right = insert(root.right, key, value)

    else:
        root.value = value  

    return root


def search(root: Optional[Node], key: int) -> Optional[str]:

    if root is None:
        return None
    
    if root.key == key:
        return root.value
    
    if key < root.key:
        return search(root.left, key)
    else:
        return search(root.right, key)


def inorder(root: Optional[Node]):

    if root:
        inorder(root.left)
        print(f"{root.key}: {root.value}")
        inorder(root.right)
