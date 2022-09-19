from corebusiness.entities.Application import Application
from corebusiness.entities.Customer import Customer
from corebusiness.exceptions.CustomerNotFoundExeption import CustomerNotFoundExeption
from corebusiness.exceptions.ValidationExeption import ValidationExeption

from ..ports.secondary.ICustomerRepository import ICustomerRepository
from ..ports.secondary.ILoanApplicationRepository import ILoanApplicationRepository
from ..ports.primary.ISubmitLoanApplication import LoanApplicationResult, ISubmitLoanApplication, LoanApplicationInfo


class SubmitLoanApplicationUseCase(ISubmitLoanApplication):
    """
    Submit a loan application
    """

    loan_application_repository: ILoanApplicationRepository = None
    customer_repository: ICustomerRepository = None

    def __init__(self, customer_repository: ICustomerRepository, loan_application_repository: ILoanApplicationRepository):
        self.customer_repository = customer_repository
        self.loan_application_repository = loan_application_repository

    def handle(self, application_info: LoanApplicationInfo):
        """
            This contains the business logic to submit an application:
            - 1. get the customer if one already exists, save one otherwise
            - 2. save the application information
            - 3. return the application ID and whether it was a success

            Whoever calls this use case must pass in an `application_info`.

            `application_info` contains the application information to be saved.
        """

        # 1. get or create the customer
        try:
            saved_customer = self.customer_repository.get_customer(application_info.customer_ssn)
        except CustomerNotFoundExeption:
            customer = Customer(None, application_info.applicant_name, application_info.customer_ssn)

            # make sure the customer information is valid
            if not customer.is_valid():
                raise ValidationExeption('Customer is not valid.')

            saved_customer = self.customer_repository.save_customer(customer)

        # 2. save the application
        application = Application(None, application_info.application_date, saved_customer.id)

        # make sure the application information is valid
        if not application.is_valid():
            raise ValidationExeption('Application is not valid.')

        try:
            saved_application = self.loan_application_repository.save_application(application)
        except Exception as err:
            # TODO: handle this error using a service, e.g. this.log_service.log(err)
            print(err)
            return LoanApplicationResult(None, False)

        # 3. return the application result
        return LoanApplicationResult(saved_application.id, True)
