from dataclasses import dataclass
from typing import Union

@dataclass
class Application:
    id: Union[str, None] = None
    date: str = ""
    customer_id: str = ""

    def is_valid(self) -> bool:
        # do some business logic validation here
        return True
