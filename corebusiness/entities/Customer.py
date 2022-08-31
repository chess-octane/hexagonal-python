from typing import Union

class Customer:
    id: Union[str, None] = None
    name: str = ''
    ssn: str = ''

    def __init__(self, id, name, ssn):
        self.id = id
        self.name = name
        self.ssn = ssn

    def is_valid(self) -> bool:
        # do some business logic validation here
        return True
