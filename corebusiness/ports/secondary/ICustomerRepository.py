import abc
from abc import abstractmethod
from ...entities.Customer import Customer


class ICustomerRepository(abc.ABC):
    @abstractmethod
    def save_customer(self, customer: Customer) ->  Customer:
        raise NotImplementedError()

    @abstractmethod
    def get_customer(self, customer_ssn: str) -> Customer:
        """
        This might throw CustomerNotFoundExeption
        """
        raise NotImplementedError()
