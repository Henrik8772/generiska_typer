from typing import TypeVar, Generic
T = TypeVar('T')


class Stack(Generic[T]):
    def __init__(self, items: list):
        self.items = items

    def push(self, item: T)
