from corebusiness.exceptions.CustomerNotFoundExeption import CustomerNotFoundExeption
from corebusiness.ports.secondary.ICustomerRepository import ICustomerRepository
from corebusiness.entities.Customer import Customer

from .db import get_connection


class CustomerRepositoryPsycopg(ICustomerRepository):
    def save_customer(self, customer: Customer) ->  Customer:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO myapp_customer (name, ssn) VALUES (%s, %s) RETURNING id", [customer.name, customer.ssn])
            customer_id = cursor.fetchone()[0]
            cursor.close()

        return Customer(
            id=customer_id,
            ssn=customer.ssn,
            name=customer.name,
        )

    def get_customer(self, customer_ssn: str) -> Customer:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, name, ssn FROM myapp_customer WHERE ssn=%s", [customer_ssn])
            customer_row = cursor.fetchone()
            cursor.close()

        if not customer_row:
            raise CustomerNotFoundExeption()

        customer = Customer(
            id=customer_row[0],
            name=customer_row[1],
            ssn=customer_row[2],
        )

        return customer
