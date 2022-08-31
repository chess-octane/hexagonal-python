from corebusiness.entities.Application import Application
from corebusiness.entities.Customer import Customer
from corebusiness.exceptions.CustomerNotFoundExeption import CustomerNotFoundExeption
from corebusiness.exceptions.ValidationExeption import ValidationExeption

from ..ports.secondary.ICustomerRepository import ICustomerRepository
from ..ports.secondary.IApplicationRepository import IApplicationRepository
from ..ports.primary.ISubmitApplication import ApplicationResult, ISubmitApplication, ApplicationInfo


class SubmitApplicationUseCase(ISubmitApplication):
    application_repository: IApplicationRepository = None
    customer_repository: ICustomerRepository = None

    def __init__(self, customer_repository: ICustomerRepository, application_repository: IApplicationRepository):
        self.customer_repository = customer_repository
        self.application_repository = application_repository

    def handle(self, application_info: ApplicationInfo):
        """
        All the business logic to submit an application goes here:
            - get the customer if one already exists
            - create one otherwise
            - create an application
            - return the end result
        """
        try:
            saved_customer = self.customer_repository.get_customer(application_info.customer_ssn)
        except CustomerNotFoundExeption:
            customer = Customer(None, application_info.applicant_name, application_info.customer_ssn)

            if not customer.is_valid():
                raise ValidationExeption('Customer is not valid.')

            saved_customer = self.customer_repository.save_customer(customer)

        application = Application(None, application_info.application_date, saved_customer.id)
        if not application.is_valid():
            raise ValidationExeption('Application is not valid.')

        try:
            saved_application = self.application_repository.save_application(application)
            return ApplicationResult(saved_application.id, True)
        except Exception as err:
            print(err)

        return ApplicationResult(None, False)
