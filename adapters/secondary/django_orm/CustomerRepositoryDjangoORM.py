from corebusiness.exceptions.CustomerNotFoundExeption import CustomerNotFoundExeption
from corebusiness.ports.secondary.ICustomerRepository import ICustomerRepository
from corebusiness.entities.Customer import Customer

from adapters.primary.django.myapp.models import Customer as CustomerModel


class CustomerRepositoryDjangoORM(ICustomerRepository):
    def save_customer(self, customer: Customer) ->  Customer:
        customer_instance = CustomerModel.objects.create(
            ssn=customer.ssn,
            name=customer.name,
        )
        return Customer(
            id=customer_instance.id,
            ssn=customer_instance.ssn,
            name=customer_instance.name,
        )

    def get_customer(self, customer_ssn: str) -> Customer:
        customer_instance = CustomerModel.objects.filter(ssn=customer_ssn).first()

        if not customer_instance:
            raise CustomerNotFoundExeption()

        return Customer(
            id=customer_instance.id,
            ssn=customer_instance.ssn,
            name=customer_instance.name,
        )
