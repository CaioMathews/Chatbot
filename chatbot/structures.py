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
        return self.messages[-1] if self.messages else None


# =====================
# Árvore AVL 
# =====================

@dataclass
class Node:
    key: int
    value: str
    left: Optional["Node"] = None
    right: Optional["Node"] = None
    height: int = 0  


def get_height(node: Optional[Node]) -> int:
    return node.height if node else -1  


def get_balance(node: Optional[Node]) -> int:
    if not node:
        return 0
    return get_height(node.right) - get_height(node.left)



def rotate_left(unbalanced: Node) -> Node:
    new_root = unbalanced.right
    orphan_subtree = new_root.left

    new_root.left = unbalanced
    unbalanced.right = orphan_subtree

    unbalanced.height = max(get_height(unbalanced.left), get_height(unbalanced.right)) + 1
    new_root.height = max(get_height(new_root.left), get_height(new_root.right)) + 1

    return new_root


def rotate_right(unbalanced: Node) -> Node:
    new_root = unbalanced.left
    orphan_subtree = new_root.right

    new_root.right = unbalanced
    unbalanced.left = orphan_subtree

    unbalanced.height = max(get_height(unbalanced.left), get_height(unbalanced.right)) + 1
    new_root.height = max(get_height(new_root.left), get_height(new_root.right)) + 1

    return new_root


def insert_node(root: Optional[Node], key: int, value: str) -> Node:

    if root is None:
        return Node(key, value)

    if key < root.key:
        root.left = insert_node(root.left, key, value)
    elif key > root.key:
        root.right = insert_node(root.right, key, value)
    else:
        root.value = value
        return root

    root.height = max(get_height(root.left), get_height(root.right)) + 1

    balance = get_balance(root)

    if balance < -1 and key < root.left.key:  
        return rotate_right(root)

    if balance > 1 and key > root.right.key:  
        return rotate_left(root)

    if balance < -1 and key > root.left.key:  
        root.left = rotate_left(root.left)
        return rotate_right(root)

    if balance > 1 and key < root.right.key:  
        root.right = rotate_right(root.right)
        return rotate_left(root)

    return root



def find_node(root: Optional[Node], key: int) -> Optional[str]:

    if root is None:
        return None
    
    if key == root.key:
        return root.value
    
    if key < root.key:
        return find_node(root.left, key)
    
    return find_node(root.right, key)


def print_inorder(root: Optional[Node]):

    if root:
        print_inorder(root.left)
        print(f"{root.key}: {root.value} (altura={root.height})")
        print_inorder(root.right)