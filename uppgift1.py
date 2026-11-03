from typing import TypeVar, Generic
T = TypeVar('T')


class Box(Generic[T]):
    def __init__(self, value: T):
        self.value = value

    def getvalue(self) -> T:
        return self.value


int_box = Box[int](10)
str_box = Box[str]("Hej")


print(int_box.getvalue().bit_count())
print(str_box.getvalue())
