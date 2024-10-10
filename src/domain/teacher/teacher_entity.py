from typing import Optional


class Teacher:

    id: Optional[int] = None
    name: str

    def __init__(self, name: str, id: Optional[int] = None):
        self.id = id
        self.name = name
