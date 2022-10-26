from dataclasses import dataclass
import abc
from abc import abstractmethod


@dataclass
class LoanApplicationInfo:
    customer_ssn: str = ""
    customer_name: str = ""
    application_date: str = ""


@dataclass
class LoanApplicationResult:
    application_id: str = ""
    success: bool = False


class ISubmitLoanApplication(abc.ABC):
    @abstractmethod
    def handle(self, application_info: LoanApplicationInfo) -> LoanApplicationResult:
        raise NotImplementedError()
