from typing import Union

class Application:
    id: Union[str, None] = None
    date: str = ""
    customer_id: str = ""

    def __init__(self, id, date, customer_id):
        self.id = id
        self.date = date
        self.customer_id = customer_id

    def is_valid(self) -> bool:
        # do some business logic validation here
        return True
