import abc
from abc import abstractmethod

class LoanApplicationInfo:
    customer_ssn: str = ""
    customer_name: str = ""
    application_date: str = ""

    def __init__(self, customer_ssn: str, customer_name: str, application_date: str):
        self.applicant_name = customer_name
        self.customer_ssn = customer_ssn
        self.application_date = application_date


class LoanApplicationResult:
    application_id: str = ""
    success: bool = False

    def __init__(self, application_id: str, success: bool):
        self.application_id = application_id
        self.success = success


class ISubmitLoanApplication(abc.ABC):
    @abstractmethod
    def handle(self, application_info: LoanApplicationInfo) -> LoanApplicationResult:
        raise NotImplementedError()
