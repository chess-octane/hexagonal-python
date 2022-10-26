from dataclasses import dataclass
from typing import Union

@dataclass
class Customer:
    id: Union[str, None] = None
    name: str = ''
    ssn: str = ''

    def is_valid(self) -> bool:
        # do some business logic validation here
        return True
